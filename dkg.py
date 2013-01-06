import random
from ctypes import cdll

secretshare = 683425

def dkg():
  #Loading the library containing the DKG node
  
  libnode = cdll.LoadLibrary('./so/libnode.so.1.0')
  
  #main is the main function in node.cc. To prevent errors, the library was created without BLSclient.o
  
  #libnode.main(7, "./node 6401 ../src/certs/1.pem ../src/certs/1-key.pem contlist 0 0 0")
  secretshare = random.random()
  
def share():
  return secretshare
