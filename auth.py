def auth(username, password):
  parse = re.search("([\w\.]*[\w])[@]([\w.]*[\w])", username)
  uname = parse.group(1)
  domain_name = parse.group(2)
  if domain_name == "gmail.com":
    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    log = mailserver.login(username,password)
    result = "true"
    mailserver.close()
  else:
    print("Sorry, " + domain_name + " is not supported. Currently only Gmail authentication is available\n")
    return "false", ""
  return result, uname, log
