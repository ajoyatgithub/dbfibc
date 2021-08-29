#!/usr/bin/env python
import smtplib
import re


def auth(username, password, auth_type):
    if auth_type == '1':
        parse = re.search("([\w\.]*[\w])[@]([\w.]*[\w])", username)
        if parse == None:
            result = "Invalid email address"
            return result
            return "S"
        uname = parse.group(1)
        domain_name = parse.group(2)
        try:
            if domain_name == "gmail.com":
                mailserver = smtplib.SMTP("smtp.gmail.com", 587)
                mailserver.ehlo()
                mailserver.starttls()
                mailserver.ehlo()
                (code, msgstr) = mailserver.login(username, password)
                if code == 235:
                    result = "S"
                else:
                    result = msgstr
                mailserver.close()
            elif domain_name == "yahoo.com":
                mailserver = smtplib.SMTP("smtp.mail.yahoo.com")
                mailserver.ehlo()
                # mailserver.starttls()
                mailserver.ehlo()
                (code, msgstr) = mailserver.login(username, password)
                if code == 235:
                    result = "S"
                else:
                    result = msgstr
                mailserver.close()
            elif domain_name == "hotmail.com":
                mailserver = smtplib.SMTP("smtp.live.com", 25)
                mailserver.ehlo()
                mailserver.starttls()
                mailserver.ehlo()
                (code, msgstr) = mailserver.login(username, password)
                if code == 235:
                    result = "S"
                else:
                    result = msgstr
                mailserver.close()
            elif domain_name == "rediffmail.com":
                mailserver = smtplib.SMTP("smtp.rediffmail.com", 25)
                # mailserver.ehlo()
                # mailserver.starttls()
                mailserver.ehlo()
                (code, msgstr) = mailserver.login(username, password)
                if code == 235:
                    result = "S"
                else:
                    result = msgstr
                mailserver.close()
            else:
                print("Sorry, " + domain_name + " is not supported. Currently only GMail authentication is available\n")
                result = "Unsupported"
        except Exception as e:
            result = e
    elif auth_type == '2':
        result = "LDAP coming soon"
    else:
        result = "Invalid"
    return result
