import threading
import subprocess
from ctypes import cdll

def dkg():
  threading.Thread(target=startdkg).start()
  
def startdkg():
  print "DKG started"
  subprocess.call("dkg/rundkg")