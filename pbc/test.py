from ctypes import *
ibc = cdll.LoadLibrary('./libibc.so.1.0.1')
add = ibc.add()
add.restype = c_int
print add.value
strin = 'ajoy91ad@gmail.com'
ids = (c_char * 40)()
ids.value = strin
hashi = c_char_p
hash_id = ibc.hash_id_G1
hash_id.restype = c_char_p
hashi = hash_id(ids)
print "\nFrom Python : ", hashi
print add.value
print add.value
