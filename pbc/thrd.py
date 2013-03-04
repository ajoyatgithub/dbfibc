import threading
import time
import socket
import re
import string
from ctypes import *

nodeID = 1; identity = ""; tempcontlist = []; port = 1000; numNodes = 0;ip = '127.0.0.1'

def read_contlist():
  """contlist contains the node contact addresses, load it into a list"""
  fp = open("contlist", "r")
  global tempcontlist, numNodes
  """reading from contlist and adding it to list tempcontlist for searching...
  tempcontlist[1] contains the contact details for node 3, and so on.
  tempcontlist[1] is again a list where each index represents
  - - - - 0:nodeID, 1:Ip addr, 2:Port num, 3:cert file for tls,
  - - - - 4:optional L to identify the leader
  numNodes tracks the total entries in contlist"""
  while 1:
    line = fp.readline()
    if not line:
      break
    numNodes += 1
    parse = re.search("([\S]+)\s([\S]+)\s([\S]+)\s([\S]+)\s([L]*)", line)
    tempcontlist.append([parse.group(1), parse.group(2), parse.group(3), parse.group(4), parse.group(5)])
  fp.close()
  """Easiest way to retreive from tempcontlist
  jl = tempcontlist[int(nodeID)-1]
  print jl[2]"""

def read_identity():
  """identity contains the node ID in line 1 and the user ID in line 2"""  
  fp = open("identity", "r")
  global nodeID, identity
  n = fp.readline()
  nodeID = n.rstrip('\r\n')
  i = fp.readline()
  identity = i.rstrip('\r\n')
  fp.close()

def listen():
  """This socket will listen for IBCRequests and IBCReply messages"""
  global port, ip
  servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    servsock.bind(('', int(port)))
  except Exception, e:
    print "Error : ", e
  servsock.listen(5)
  while True:
    #print "Waiting for connection"
    conn, address = servsock.accept()
    #print "connection from ", address
    #print "Waiting for message"
    msg = conn.recv(1024)
    parse_msg(msg)
  conn.close()
  servsock.close()
  return

def ibc_request_recv(stringid, nodeid):
  ibc = cdll.LoadLibrary('./libibc.so.1.0.1')
  hash_id = ibc.hash_id_G1
  hash_id.restype = c_char_p
  c_id = (c_char * 40)()
  c_id.value = stringid
  ibc.hash_id_G1(c_id)
  #ibc.keyshare(parseid.group(1))  


def parse_msg(msgstr):
  parse = re.search("([\w]+):(.*)", msgstr)
  if parse == None:
    print "Received invalid message : ", msgstr
  elif parse.group(1) == "IBC_REQUEST":
    parseid = re.search("([\S]+):([\S]+)(:END)", parse.group(2))
    if parseid == None:
      print "Invalid IBC request : ", parse.group(2)
    else:
      print "Received : IBC request for the id ", parseid.group(1) + " from " + parseid.group(2)
      ibc_request_recv(parseid.group(1), parseid.group(2))

  elif parse.group(1) == "IBC_REPLY":
    print "Received : IBC reply message"

def sendRequest():
  """This socket will send IBC_REQUEST messages"""
  global tempcontlist, numNodes, nodeID, port
  for i in range(numNodes):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    [nodeid, c_ip, c_port, cert_file, l] = tempcontlist[i]
    if c_port == port:
      continue
      
    #print "i ", nodeID, "am trying to connect to ", nodeid, "at ", c_ip, int(c_port), c_port
    try:
      sock.connect((c_ip, int(c_port)))
    except Exception, e:
      print "Unable to send : ", e, c_ip, c_port
      continue;
    msg = "IBC_REQUEST:" + identity + ":" + nodeID + ":END"
    print "Sent : ", msg
    sock.sendall(msg)
    sock.close()
  return
  

def main():
  global port, ip, nodeID
  read_contlist()
  read_identity()
  li = tempcontlist[int(nodeID) - 1]
  ip = li[1]
  port = li[2]
  threading.Thread(target=listen).start()
  option = input("Enter 1 to send request : ")

  if option == 1:
    threading.Thread(target=sendRequest).start()

  """r = input("Which row do you wish to print : ")
  r = r - 1
  print tempcontlist[r]"""

  
if __name__ == "__main__":
  main()
