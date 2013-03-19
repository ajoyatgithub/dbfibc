import re
from ctypes import *
u = ""
fp = open("system.param","r")
n = fp.readline()
t = fp.readline()
f = fp.readline()
p = fp.readline()
u = fp.readline()
fp.close()
pr = re.search("(U)\s(.*)", u)
if pr==None:
  print("Corrupted system.param(U). About to quit.")
else:
  u = pr.group(2)

test1 = cdll.LoadLibrary('./libtest1.so.1.0.1')
print "U is ", u, len(u)
globalu = (c_char * 310)()
globalu.value = u
test1.init_pairing(5, 1, 0)
test1.readg(globalu)