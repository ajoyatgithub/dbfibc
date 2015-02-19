#import threading
import subprocess
import os
import re
import threading
import pyinotify

nodeid = 0
tempcontlist = []
status = "nosecret"

def onChange(ev):
  global status
  status = "sharegen"

def watch_secrets():
  wm = pyinotify.WatchManager()
  wm.add_watch('files/secrets', pyinotify.IN_CLOSE_WRITE, onChange)
  notifier = pyinotify.Notifier(wm)
  notifier.loop()
  
def dkg(nid):
  global nodeid
  #print "DKG starting...."
  threading.Thread(target=startdkg).start()
  threading.Thread(target=watch_secrets).start()
  #print "DKG started...."
  #startdkg()
  
def startdkg():
  global nodeid
  fp = open("files/contlist","r")
  while 1:
    line = fp.readline()
    if not line:
      break
    parse = re.search("([\S]+)\s([\S]+)\s([\S]+)\s([\S]+)\s([L]*)", line)
    tempcontlist.append([parse.group(1), parse.group(2), parse.group(3), parse.group(4), parse.group(5)])
  fp.close()
  [nid, c_ip, c_port, cert_file, l] = tempcontlist[int(nodeid)-1]
  ltr = "./dkg/node %d certs/%d.pem certs/%d-key.pem files/contlist 0 0 0" % (int(c_port), int(nid), int(nid))
  print nodeid, ltr
  #fp = open("dkg/rundkg","w")
  #fp.write(ltr)
  #fp.close()
  #ltr = "../dkg/node %d ../dkg/certs/%d.pem ../dkg/certs/%d-key.pem ../dkg/contlist 0 0 0" % (int(c_port), int(nid), int(nid))
  #print ltr
  #os.chdir("dkg/")
  subprocess.call(ltr)