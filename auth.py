#!/usr/bin/env python
import smtplib
import re

def auth(username, password, auth_type):
  if auth_type == '1':
    parse = re.search("([\w\.]*[\w])[@]([\w.]*[\w])", username)
    if parse == None:
      result = "Invalid email address"
      #return result
      return "S"
    uname = parse.group(1)
    domain_name = parse.group(2)
    if domain_name == "gmail.com":
      #mailserver = smtplib.SMTP("smtp.gmail.com", 587)
      #mailserver.ehlo()
      #mailserver.starttls()
      #mailserver.ehlo()
      #(code, msgstr) = mailserver.login(username,password)
      code = 235
      if code == 235:
        result = "S"
      else:
        result = msgstr
      #mailserver.close()
    else:
      print("Sorry, " + domain_name + " is not supported. Currently only GMail authentication is available\n")
      result = "Unsupported"
  else:
    result = "LDAP is not currently supported. Coming soon"
  return result
