#cc ibcfuncs.c -o ibc.o -lpbc -lgmp -lcrypto
#ar rcs libibc.a ibc.o
rm -rf libibc.so.1.0.1 ibc.o
cc -c -fPIC ibcfuncs.c -lcrypto -lpbc -lgmp -o ibc.o
cc -shared ibc.o -lcrypto -lpbc -lgmp -Wl,-soname,libibc.so.1 -o libibc.so.1.0.1
