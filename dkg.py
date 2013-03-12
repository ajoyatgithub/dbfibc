import threading
import subprocess
from ctypes import cdll

def dkg():
  threading.Thread(target=startdkg).start()
  
def startdkg():
  print "DKG started"
  out = subprocess.check_output(['./dkg/node', '8901', 'dkg/certs/1.pem', 'dkg/certs/1-key.pem', 'dkg/contlist', '0', '0', '0'])
  print "DKG finishes... Out is"
  print out