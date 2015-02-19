cc -c -fPIC test1.c -lcrypto -lpbc -lgmp -o test1.o
cc -shared test1.o -lcrypto -lpbc -lgmp -Wl,-soname,libtest1.so.1 -o libtest1.so.1.0.1
