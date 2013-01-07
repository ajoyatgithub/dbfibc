import random
import threading
from ctypes import cdll

secretshare = 683425

def dkg():
  #Loading the library containing the DKG node
  
  libnode = cdll.LoadLibrary('./so/libnode.so.1.0')
  
  #main is the main function in node.cc. To prevent errors, the library was created without BLSclient.o
  
  libnode.main()
  #libnode.main(5, "./node 6401 ../src/certs/1.pem ../src/certs/1-key.pem contlist")
  secretshare = random.random()
  
def share():
  secretshare = random.random()
  return secretshare
  

class MyThread ( threading.Thread ):
   def run ( self ):
      print 'Insert some thread stuff here.'
      print 'It'll be executed...yeah....'
      print 'There's not much to it.'

MyThread().start()
