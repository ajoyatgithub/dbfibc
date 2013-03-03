cc simplepbc.c -o ibc.o -lpbc -lgmp -lcrypto
ar rcs libibc.a ibc.o
cc -c -fPIC simplepbc.c -o ibc.o -lcrypto -lpbc -lgmp
cc -shared -Wl,-soname,libibc.so.1 -o libibc.so.1.0.1 ibc.o

