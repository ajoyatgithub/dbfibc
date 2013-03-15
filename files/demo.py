import re
fp = open("contlist","r")
tempcontlist = []
while 1:
  line = fp.readline()
  if not line:
    break
  parse = re.search("([\S]+)\s([\S]+)\s([\S]+)\s([\S]+)\s([L]*)", line)
  tempcontlist.append([parse.group(1), parse.group(2), parse.group(3), parse.group(4), parse.group(5)])
fp.close()

def pr(i):
  [nid, c_ip, c_port, cert_file, l] = tempcontlist[int(i)-1]
  ltr = "./node %d certs/%d.pem certs/%d-key.pem ../files/contlist 0 0 0" % (int(c_port), int(nid), int(nid))
  print ltr

while 1:
  op = input("Enter from 1 to 10 : ")
  pr(op)
