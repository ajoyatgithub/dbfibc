#!/usr/bin/env python
import auth
import dkg
import ibc
import sys
import getpass
import sys

nodeid = 0

def readlist():
  global nodeid
  fp = open("files/identity","r")
  i = fp.readline()
  nodeid = i.rstrip('\r\n')
  print "Read nodeid just now. nodeid =", nodeid
  fp.close()

def main():
  print "**************WELCOME****************\n"
  print "This is the interface for the program\n"
  readlist()
  #Phase 1 - Authenticating the identity. The following code will retreive the username and password and send it to the module auth.py
  
  auth_type = raw_input("Please select the type of authentication(Enter the number and press enter) \n\t1. Email\n\t2. LDAP\n\t\t:")
  if auth_type == '1':
    auth_str = "Email address"
  elif auth_type == '2':
    auth_str = "LDAP username"
  else:
    print "Invalid input"
    sys.exit()
  print "Please enter the " + auth_str + " that you want to use as your identity : "
  username = raw_input(auth_str + " : ")
  password = getpass.getpass("Please enter the password for your " + auth_str + " '" + username + "' : ")
  auth_result = auth.auth(username, password, auth_type)
  auth_result = "S"
  if  auth_result is "S":
    print("Hello, " + username + ". Authentication has been successful. You can now use your username as your Identity\n")
  else:
    print("Authentication failed")
    print auth_result
    return
  
  #Phase 2 - The DKG protocol can now start. It will run in a different thread. As soon as DKG completes, the share is written to a file
  print("Please wait while the system initializes")
  global nodeid
  #print "Calling DKG, node id is ", nodeid
  dkg.dkg(nodeid)
  print("DKG completed")
  
  #Phase 3 - Generate the keys using username and the share, the keys are stored in the loaded ibc library
  ibc.start(username, nodeid)
  print("Successfully created both public as well as the private keys")
  
  #Phase 4 - Applications. the generated keys can be used to encrypt as well as decrypt messages
  option = raw_input("Select what you would like to do : \n1. Encrypt\t2. Decrypt\n\t: ")
  if option == '1':
  	ibc.encrypt()
  elif option == '2':
  	ibc.decrypt()
  else:
    print("Incorrect option")
    return
  print("Exiting................")
  return

class NullWriter:
    def write(self, s):
        pass
          
#sys.stderr = NullWriter()

if __name__ == "__main__":
  main()
