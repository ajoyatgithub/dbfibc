#!/usr/bin/env python
import argparse
import string
import md5
import auth
import dkg
import ibc
import app
import sys
from ctypes import cdll

def main():
  print "**************WELCOME****************\n"
  print "This is the interface for the program\n"
  libnode = cdll.LoadLibrary('../dkkg/libnode.so.1.0')
  print libnode.main(8, "./node 6401 ../src/certs/1.pem ../src/certs/1-key.pem contlist 0 0 0")
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
  
  print("Your public key is now" + ibc.ibc(username, dkg.dkg(), dkg.dkg()))

class NullWriter:
    def write(self, s):
        pass
          
#sys.stderr = NullWriter()

if __name__ == "__main__":
  main()
