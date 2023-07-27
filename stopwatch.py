
import datetime
import threading
import time
from tp_client import *
from logging import (getLogger, Formatter, NullHandler, FileHandler, StreamHandler, DEBUG, INFO, WARNING)

g_log = getLogger()




class StopWatch:
    def __init__(self) -> None:
        self.running = {}
        self.elapsed_times = {}
        self.paused_times = {}
        self.start_times = {}

    def run_stopwatch(self, stopwatch_id, resume_stopwatch = False):
        TPClient.createState(stateId=f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", description=f"SW | Time Elapsed {stopwatch_id}", value="00:00:00", parentGroup=f"SW | {stopwatch_id}")
        TPClient.createState(stateId=f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", description=f"SW | Status {stopwatch_id}", value="RUNNING", parentGroup=f"SW | {stopwatch_id}")

        if stopwatch_id not in self.elapsed_times:
            self.elapsed_times[stopwatch_id] = datetime.timedelta()
            self.start_times[stopwatch_id] = time.time()

        if self.running.get(stopwatch_id, False):
            return

        if resume_stopwatch:
            g_log.info(f"Resuming stopwatch {stopwatch_id}")
            ## Checking where we left off.. - perhaps we should set to 0 everytime since we starting not resuming??
            self.start_times[stopwatch_id] = time.time() - (self.paused_times.get(stopwatch_id, datetime.timedelta()).total_seconds())
            self.paused_times[stopwatch_id] = datetime.timedelta() # reset paused time
        

        ## Setting to Running
        self.running[stopwatch_id] = True
        start_time = self.start_times[stopwatch_id] #Pulling the Start time from the dictionary
        
        while self.running[stopwatch_id]:
            elapsed_time = datetime.timedelta(seconds=round(time.time() - start_time))
            elapsed_time_str = str(elapsed_time)
            self.elapsed_times[stopwatch_id] = elapsed_time
            
            g_log.info(f"Stopwatch {stopwatch_id}: {elapsed_time_str}")
            TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", str(elapsed_time_str))
            
            time.sleep(1)


    def start_stopwatch(self, stopwatch_id, resume_stopwatch=False):
        """ 
        This runs the stopwatch in a separate thread.
        """
        t = threading.Thread(target=self.run_stopwatch, args=(stopwatch_id, resume_stopwatch), daemon=True)
        t.start()


    def pause_stopwatch(self, stopwatch_id):
        if not self.running.get(stopwatch_id, False):
            return
        
        self.running[stopwatch_id] = False
        paused_time = datetime.timedelta(seconds=round(time.time() - self.start_times[stopwatch_id]))
        
        if stopwatch_id not in self.paused_times:
            self.paused_times[stopwatch_id] = datetime.timedelta()
            
        self.paused_times[stopwatch_id] += paused_time
        g_log.info(f"Stopwatch {stopwatch_id} paused: {self.paused_times[stopwatch_id]}")
        TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "PAUSED")



    def reset_stopwatch(self, stopwatch_id):
        self.running[stopwatch_id] = False
        TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", "0:00:00")
        TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "RESET")

        del self.start_times[stopwatch_id]
        del self.elapsed_times[stopwatch_id]
        del self.paused_times[stopwatch_id]


SW = StopWatch()






























## backup before class running = {}
## backup before class elapsed_times = {}
## backup before class paused_times = {}
## backup before class start_times = {}
## backup before class 
## backup before class 
## backup before class 
## backup before class 
## backup before class 
## backup before class def stopwatch(stopwatch_id, resume_stopwatch=False):
## backup before class     global running, elapsed_times, start_times
## backup before class     
## backup before class     
## backup before class     TPClient.createState(stateId=f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", description=f"Time Elapsed {stopwatch_id}", value="00:00:00", parentGroup=f"SW | {stopwatch_id}")
## backup before class     TPClient.createState(stateId=f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", description=f"Status {stopwatch_id}", value="RUNNING", parentGroup=f"SW | {stopwatch_id}")
## backup before class 
## backup before class     if stopwatch_id not in elapsed_times:
## backup before class         elapsed_times[stopwatch_id] = datetime.timedelta()
## backup before class         start_times[stopwatch_id] = time.time()
## backup before class 
## backup before class     if running.get(stopwatch_id, False):
## backup before class         return
## backup before class     
## backup before class     if resume_stopwatch:
## backup before class         print(stopwatch_id, " has resumed")
## backup before class         ## Checking where we left off.. - perhaps we should set to 0 everytime since we starting not resuming??
## backup before class         start_times[stopwatch_id] = time.time() - (paused_times.get(stopwatch_id, datetime.timedelta()).total_seconds())
## backup before class         paused_times[stopwatch_id] = datetime.timedelta() # reset paused time
## backup before class     
## backup before class     ## Setting to Running
## backup before class     running[stopwatch_id] = True
## backup before class     start_time = start_times[stopwatch_id] #Pulling the Start time from the dictionary
## backup before class 
## backup before class     while running[stopwatch_id]:
## backup before class         elapsed_time = datetime.timedelta(seconds=round(time.time() - start_time))
## backup before class         elapsed_times[stopwatch_id] = elapsed_time
## backup before class         elapsed_time_str = str(elapsed_time)
## backup before class 
## backup before class         print(f"Stopwatch {stopwatch_id}: {elapsed_time_str}")
## backup before class         TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", str(elapsed_time_str))
## backup before class 
## backup before class         time.sleep(1)
## backup before class 
## backup before class 
## backup before class 
## backup before class def start_stopwatch(stopwatch_id, resume_stopwatch=False):
## backup before class     t = threading.Thread(target=stopwatch, args=(stopwatch_id,resume_stopwatch), daemon=True)
## backup before class     t.start()
## backup before class 
## backup before class 
## backup before class def pause_stopwatch(stopwatch_id):
## backup before class     global paused_times, running, start_times, running
## backup before class     
## backup before class     if not running.get(stopwatch_id, False):
## backup before class         return
## backup before class     
## backup before class     running[stopwatch_id] = False
## backup before class     paused_time = datetime.timedelta(seconds=round(time.time() - start_times[stopwatch_id]))
## backup before class     
## backup before class     if stopwatch_id not in paused_times:
## backup before class         paused_times[stopwatch_id] = datetime.timedelta()
## backup before class         
## backup before class     paused_times[stopwatch_id] += paused_time
## backup before class     
## backup before class     print(f"Stopwatch {stopwatch_id} paused: {paused_times[stopwatch_id]}")
## backup before class     TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "PAUSED")
## backup before class 
## backup before class 
## backup before class 
## backup before class 
## backup before class def stop_stopwatch(stopwatch_id):
## backup before class     global elapsed_times, running, paused_times
## backup before class 
## backup before class     running[stopwatch_id] = False
## backup before class     elapsed_time = elapsed_times[stopwatch_id] + paused_times.get(stopwatch_id, datetime.timedelta())
## backup before class     elapsed_time_str = str(elapsed_time)
## backup before class 
## backup before class     print(f"Stopwatch {stopwatch_id} stopped: {elapsed_time_str}")
## backup before class     TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", str(elapsed_time_str))
## backup before class     TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "STOPPED")
## backup before class 
## backup before class     elapsed_times[stopwatch_id] = datetime.timedelta()
## backup before class     paused_times[stopwatch_id] = datetime.timedelta()











# import datetime
# import threading
# import time
# 
# from tp_client import *
# 
# running = {}
# decimals = {}
# elapsed_times = {}
# paused_times = {}
# start_times = {}
# 
# 
# def stopwatch(stopwatch_id):
#     global running, elapsed_times, start_times
# 
#     TPClient.createState(stateId=f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", description=f"Time Elapsed {stopwatch_id}", value="00:00:00", parentGroup=f"SW | {stopwatch_id}")
#     TPClient.createState(stateId=f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", description=f"Status {stopwatch_id}", value="RUNNING", parentGroup=f"SW | {stopwatch_id}")
# 
#     if stopwatch_id not in elapsed_times:
#         elapsed_times[stopwatch_id] = datetime.timedelta()
#         start_times[stopwatch_id] = time.time()
# 
#     if running.get(stopwatch_id, False):
#         return
# 
#     running[stopwatch_id] = True
#     start_time = start_times[stopwatch_id]
# 
#     while running[stopwatch_id]:
#         elapsed_time = datetime.timedelta(seconds=round(time.time() - start_time))
#         elapsed_times[stopwatch_id] = elapsed_time
#         elapsed_time_str = str(elapsed_time)
# 
#         print(f"Stopwatch {stopwatch_id}: {elapsed_time_str}")
#         TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", str(elapsed_time_str))
# 
#         time.sleep(1)
# 
# 
# def reset_stopwatch(stopwatch_id):
#     global elapsed_times, start_times
# 
#     if stopwatch_id in elapsed_times:
#         del elapsed_times[stopwatch_id]
# 
#     if stopwatch_id in start_times:
#         del start_times[stopwatch_id]
# 
#     TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", "00:00:00")
#     TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "RESET")
# 
# 
# def start_stopwatch(stopwatch_id):
#     t = threading.Thread(target=stopwatch, args=(stopwatch_id,), daemon=True)
#     t.start()
# 
# 
# 
# def stop_stopwatch(stopwatch_id):
#     global elapsed_times
# 
#     running[stopwatch_id] = False
#     elapsed_time = elapsed_times[stopwatch_id]
#     elapsed_time_str = str(elapsed_time)
# 
#     print(f"Stopwatch {stopwatch_id} stopped: {elapsed_time_str}")
#     TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", str(elapsed_time_str))
#     TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "STOPPED")
# 
# 
# 
# def pause_stopwatch(stopwatch_id):
#     global paused_times, running
# 
#     if not running.get(stopwatch_id, False):
#         return
# 
#     running[stopwatch_id] = False
#     paused_time = datetime.timedelta(seconds=round(time.time() - start_times[stopwatch_id]))
#     paused_times[stopwatch_id] += paused_time
# 
#     print(f"Stopwatch {stopwatch_id} paused: {paused_times[stopwatch_id]}")
#     TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "PAUSED")

    
    
#def resume_stopwatch(stopwatch_id):
#    global running, start_times, paused_times
#    
#    paused_times[stopwatch_id] += datetime.datetime.now() - pause_start_times[stopwatch_id]
#    print(f"Resuming stopwatch {stopwatch_id}")
#    start_stopwatch(stopwatch_id)
#    print(f"Starting thread for stopwatch {stopwatch_id}")
#    #thread.start()
#
#    TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "RUNNING")












#-----------------------------

#Backup -  import datetime
#Backup -  import threading
#Backup -  import time
#Backup -  
#Backup -  from tp_client import *
#Backup -  
#Backup -  running = {}
#Backup -  decimals = {}
#Backup -  elapsed_times = {}
#Backup -  paused_times = {}
#Backup -  start_times = {}
#Backup -  
#Backup -  
#Backup -  def stopwatch(stopwatch_id):
#Backup -      global running, elapsed_times, start_times
#Backup -  
#Backup -      TPClient.createState(stateId=f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", description=f"Time Elapsed {stopwatch_id}", value="00:00:00", parentGroup=f"SW | {stopwatch_id}")
#Backup -      TPClient.createState(stateId=f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", description=f"Status {stopwatch_id}", value="RUNNING", parentGroup=f"SW | {stopwatch_id}")
#Backup -  
#Backup -      if stopwatch_id not in elapsed_times:
#Backup -          elapsed_times[stopwatch_id] = datetime.timedelta()
#Backup -          start_times[stopwatch_id] = time.time()
#Backup -  
#Backup -      if running.get(stopwatch_id, False):
#Backup -          return
#Backup -  
#Backup -      running[stopwatch_id] = True
#Backup -      start_time = start_times[stopwatch_id]
#Backup -  
#Backup -      while running[stopwatch_id]:
#Backup -          elapsed_time = datetime.timedelta(seconds=round(time.time() - start_time))
#Backup -          elapsed_times[stopwatch_id] = elapsed_time
#Backup -          elapsed_time_str = str(elapsed_time)
#Backup -  
#Backup -          print(f"Stopwatch {stopwatch_id}: {elapsed_time_str}")
#Backup -          TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", str(elapsed_time_str))
#Backup -  
#Backup -          time.sleep(1)
#Backup -  
#Backup -  
#Backup -  def reset_stopwatch(stopwatch_id):
#Backup -      global elapsed_times, start_times
#Backup -  
#Backup -      if stopwatch_id in elapsed_times:
#Backup -          del elapsed_times[stopwatch_id]
#Backup -  
#Backup -      if stopwatch_id in start_times:
#Backup -          del start_times[stopwatch_id]
#Backup -  
#Backup -      TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", "00:00:00")
#Backup -      TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "RESET")
#Backup -  
#Backup -  
#Backup -  def start_stopwatch(stopwatch_id):
#Backup -      t = threading.Thread(target=stopwatch, args=(stopwatch_id,), daemon=True)
#Backup -      t.start()
#Backup -  
#Backup -  
#Backup -  
#Backup -  def stop_stopwatch(stopwatch_id):
#Backup -      global elapsed_times
#Backup -  
#Backup -      running[stopwatch_id] = False
#Backup -      elapsed_time = elapsed_times[stopwatch_id]
#Backup -      elapsed_time_str = str(elapsed_time)
#Backup -  
#Backup -      print(f"Stopwatch {stopwatch_id} stopped: {elapsed_time_str}")
#Backup -      TPClient.stateUpdate(f"{PLUGIN_ID}.states.time_elapsed.{stopwatch_id}", str(elapsed_time_str))
#Backup -      TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "STOPPED")
#Backup -  
#Backup -  
#Backup -  
#Backup -  def pause_stopwatch(stopwatch_id):
#Backup -      global paused_times, running
#Backup -  
#Backup -      if not running.get(stopwatch_id, False):
#Backup -          return
#Backup -  
#Backup -      running[stopwatch_id] = False
#Backup -      paused_time = datetime.timedelta(seconds=round(time.time() - start_times[stopwatch_id]))
#Backup -      paused_times[stopwatch_id] += paused_time
#Backup -  
#Backup -      print(f"Stopwatch {stopwatch_id} paused: {paused_times[stopwatch_id]}")
#Backup -      TPClient.stateUpdate(f"{PLUGIN_ID}.states.STATUS.{stopwatch_id}", "PAUSED")












