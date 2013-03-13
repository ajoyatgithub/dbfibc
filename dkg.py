import threading
import subprocess
import os
import re

nodeid = 0
tempcontlist = []

def dkg(nid):
  global nodeid
  nodeid = nid
  threading.Thread(target=startdkg).start()
  
def startdkg():
  fp = open("files/contlist","r")
  while 1:
    line = fp.readline()
    if not line:
      break
    parse = re.search("([\S]+)\s([\S]+)\s([\S]+)\s([\S]+)\s([L]*)", line)
    tempcontlist.append([parse.group(1), parse.group(2), parse.group(3), parse.group(4), parse.group(5)])
  fp.close()
  [nid, c_ip, c_port, cert_file, l] = tempcontlist[int(nodeid)-1]
  ltr = "./node %d certs/%d.pem certs/%d-key.pem contlist 0 0 0" % (int(c_port), int(nid), int(nid))
  fp = open("dkg/rundkg","w")
  fp.write(ltr)
  fp.close()
  #ltr = "../dkg/node %d ../dkg/certs/%d.pem ../dkg/certs/%d-key.pem ../dkg/contlist 0 0 0" % (int(c_port), int(nid), int(nid))
  print ltr
  os.chdir("dkg/")
  subprocess.call('ls', shell=True)
  subprocess.call(ltr, shell=True)