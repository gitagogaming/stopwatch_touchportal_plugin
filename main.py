from tp_client import *
from argparse import ArgumentParser
from logging import (getLogger, Formatter, NullHandler, FileHandler, StreamHandler, DEBUG, INFO, WARNING)
from stopwatch import SW as s_watch
from TPPEntry import PLUGIN_ID
import threading
import time


g_log = getLogger()


def handleSettings(settings, on_connect=False):
    settings = { list(settings[i])[0] : list(settings[i].values())[0] for i in range(len(settings)) }


@TPClient.on(TP.TYPES.onConnect)
def onConnect(data):
    g_log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
    g_log.debug(f"Connection: {data}")
    if settings := data.get('settings'):
        handleSettings(settings, True)



@TPClient.on(TP.TYPES.onSettingUpdate)
def onSettingUpdate(data):
    g_log.debug(f"Settings: {data}")
    if (settings := data.get('values')):
        handleSettings(settings, False)


@TPClient.on(TP.TYPES.onAction)
def onAction(data):
    g_log.debug(f"Action: {data}")
    if data['actionId'] == PLUGIN_ID + ".act.start_stopwatch":

        if (data['data'][0]['value']) == "Start":
            s_watch.start_stopwatch((data['data'][1]['value']), resume_stopwatch = True)
                   
        if (data['data'][0]['value']) == "Pause":
            s_watch.pause_stopwatch((data['data'][1]['value']))
                
        if (data['data'][0]['value']) == "Stop" or (data['data'][0]['value']) == "Reset":
            s_watch.reset_stopwatch((data['data'][1]['value']))

        if (data['data'][0]['value']) == "Resume":
            ## This is pointless at this point in time when start will just resume it if its able, otherwise stop should reset the values to 0.
            s_watch.start_stopwatch((data['data'][1]['value']), resume_stopwatch = True)



@TPClient.on(TP.TYPES.onHold_down)
def onHold_down(data):
    g_log.debug(f"Hold down: {data}")
    while True:
        time.sleep(1)
        g_log.debug(f"Hold down: {data['data'][0]['id']}")
        ## making users wait 1 second before the we notice if its still holding down the button.
        if data['data'][0]['id'] == PLUGIN_ID + ".act.status":
            if data['data'][0]['value'] == "Reset": 
                if TPClient.isActionBeingHeld(PLUGIN_ID + '.act.start_stopwatch'):
                    try:
                        s_watch.reset_stopwatch((data['data'][1]['value']))
                    except KeyError as e:
                          g_log.error(f"{e} is not a valid stopwatch name")
                    break
            
            if data['data'][0]['value'] == "Pause":
                if TPClient.isActionBeingHeld(PLUGIN_ID + '.act.start_stopwatch'):
                    try:
                        s_watch.pause_stopwatch((data['data'][1]['value']))
                    except KeyError as e:
                        g_log.error(f"{e} is not a valid stopwatch name")
                    break
            
            if data['data'][0]['value'] == "Start":
                if TPClient.isActionBeingHeld(PLUGIN_ID + '.act.start_stopwatch'):
                    try:
                        s_watch.start_stopwatch((data['data'][1]['value']), resume_stopwatch = True)
                    except KeyError as e:
                        g_log.error(f"{e} is not a valid stopwatch name")
                    break      
        else:
            break





@TPClient.on(TP.TYPES.onShutdown)
def onShutdown(data):
    g_log.info('Received shutdown event from TP Client.')

#@TPClient.on(TP.TYPES.onError)
#def onError(exc):
#    g_log.error(f'Error in TP Client event handler: {repr(exc)}')


def main():
    global TPClient, g_log
    ret = 0  # sys.exit() value
    # handle CLI arguments
    parser = ArgumentParser()
    parser.add_argument("-d", action='store_true',
                        help="Use debug logging.")
    parser.add_argument("-w", action='store_true',
                        help="Only log warnings and errors.")
    parser.add_argument("-q", action='store_true',
                        help="Disable all logging (quiet).")
    parser.add_argument("-l", metavar="<logfile>",
                        help="Log to this file (default is stdout).")
    parser.add_argument("-s", action='store_true',
                        help="If logging to file, also output to stdout.")

    opts = parser.parse_args()
    del parser

    # set up logging
    if opts.q:
        # no logging at all
        g_log.addHandler(NullHandler())
    else:
        # set up pretty log formatting (similar to TP format)
        fmt = Formatter(
            fmt="{asctime:s}.{msecs:03.0f} [{levelname:.1s}] [{filename:s}:{lineno:d}] {message:s}",
            datefmt="%H:%M:%S", style="{"
        )
        # set the logging level
        if   opts.d: g_log.setLevel(DEBUG)
        elif opts.w: g_log.setLevel(WARNING)
        else:        g_log.setLevel(INFO)
        # set up log destination (file/stdout)
        if opts.l:
            try:
                # note that this will keep appending to any existing log file
                fh = FileHandler(str(opts.l))
                fh.setFormatter(fmt)
                g_log.addHandler(fh)
            except Exception as e:
                opts.s = True
                g_log.error(f"Error while creating file logger, falling back to stdout. {repr(e)}")
        if not opts.l or opts.s:
            sh = StreamHandler(sys.stdout)
            sh.setFormatter(fmt)
            g_log.addHandler(sh)



    try:
        TPClient.connect()
        g_log.info('TP Client closed.')
    except KeyboardInterrupt:
        g_log.warning("Caught keyboard interrupt, exiting.")
    except Exception:
        # This will catch and report any critical exceptions in the base TPClient code,
        # _not_ exceptions in this plugin's event handlers (use onError(), above, for that).
        from traceback import format_exc
        g_log.error(f"Exception in TP Client:\n{format_exc()}")
        ret = -1
    finally:
        # Make sure TP Client is stopped, this will do nothing if it is already disconnected.
        TPClient.disconnect()

    # TP disconnected, clean up.
    del TPClient

    g_log.info(f"{TP_PLUGIN_INFO['name']} stopped.")
    return ret



if __name__ == "__main__":
    sys.exit(main())

