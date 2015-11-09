#! /usr/bin/gcc
gcc -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -DMAJOR_VERSION=1 -DMINOR_VERSION=0 -I/usr/include/python2.7 -c spammodule.c -o spammodule.o
gcc -shared spammodule.o -L/usr/local/lib -o spammodule.so
