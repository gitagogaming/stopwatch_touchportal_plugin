## TP CLIENT IMPORT
import sys
import TouchPortalAPI as TP


__version__ = "2.1"
PLUGIN_ID = "tp.plugin.Gitago.Stopwatch"

# Basic plugin metadata
TP_PLUGIN_INFO = {
    'sdk': 6,
    'version': int(float(__version__) * 100),  # TP only recognizes integer version numbers
    'name': "Stopwatch",
    'id': PLUGIN_ID,
    'configuration': {
        'colorDark': "#25274c",
        'colorLight': "#707ab5"
    }
}

try:
    TPClient = TP.Client(
        pluginId = PLUGIN_ID,  
        sleepPeriod = 0.05,  
        autoClose = True,     
        checkPluginId = True,  
        maxWorkers = 4,        
        updateStatesOnBroadcast = False,  
    )
except Exception as e:
    sys.exit(f"Could not create TP Client, exiting. Error was:\n{repr(e)}")



