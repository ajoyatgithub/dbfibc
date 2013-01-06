#!/usr/bin/env python
import argparse
import string
import md5
import auth
import dkg
import ibc
import app
import sys

def main():
  print "**************WELCOME****************\n"
  print "This is the interface for the program\n"
  #Phase 1 - Authenticating the identity. The following code will retreive the username and password and send it to the module auth.py
  
  auth_type = raw_input("Please select the type of authentication(Enter the number and press enter) \n\t1. Email\n\t2. LDAP\n\t\t:")
  if auth_type == '1':
    auth_str = "Email address"
  elif auth_type == '2':
    auth_str = "LDAP username"
  print "Please enter the " + auth_str + " that you want to use as your identity : "
  username = raw_input(auth_str + " : ")
  password = raw_input("Please enter the password for your " + auth_str + " '" + username + "' : ")
  hashp = md5.new(password).digest()
  auth_result = auth.auth(username, password, auth_type)
  if  auth_result is "S":
    print("Hello, " + username + ". Authentication has been successful. You can now use your username as your Identity\n")
  else:
    print("Authentication failed : " + auth_result)
    return
  
  #Phase 2 - The DKG protocol can now start. It will run in a different thread. As soon as DKG completes, the share is returned
  print("Please wait while the system initializes")
  dkg.dkg()
  share = dkg.share()
  print("DKG completed. Your share is " + share)
  
  #Phase 3 - Generate the keys using username and the share
  ibc.generatekeys(username, share)
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
