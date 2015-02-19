import sys
import re

sys_n = 1; sys_t = 1; sys_f = 1

def read_sysparam():
  """This function will read system.param and initialize the values for n, t, f"""
  global sys_n, sys_t, sys_f
  fp = open("system.param","r")
  n = fp.readline()
  t = fp.readline()
  f = fp.readline()
  fp.close()
  n = n.rstrip('\r\n')
  t = t.rstrip('\r\n')
  f = f.rstrip('\r\n')
  pr = re.search("(n)\s(\d)", n)
  if pr==None:
    print("Corrupted system.param(n). About to quit.")
    sys.exit()
  else:
    sys_n = pr.group(2)
  pr = re.search("(t)\s(\d)", t)
  if pr==None:
    print("Corrupted system.param(t). About to quit.")
    sys.exit()
  else:
    sys_n = pr.group(2)
  pr = re.search("(f)\s(\d)", f)
  if pr==None:
    print("Corrupted system.param(t). About to quit.")
    sys.exit()
  else:
    sys_n = pr.group(2)
    
def main():
  read_sysparam()
  print "n t f"
  print sys_n, sys_t, sys_f
  
if __name__ == "__main__":
  main()