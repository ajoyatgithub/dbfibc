import pyinotify
import threading

status = "Nosecret"

def onChange(ev):
  global status
  status = "sharegen"
  print "changed"

def watch_secrets():
  wm = pyinotify.WatchManager()
  wm.add_watch('files/secrets', pyinotify.IN_CLOSE_WRITE, onChange)
  notifier = pyinotify.Notifier(wm)
  notifier.loop()

threading.Thread(target=watch_secrets).start()
while 1:
  if status == "sharegen":
    break
  else:
    print "Status is : ", status
    #pass
