from shell import shell

cmd1 = 'gcc -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c spammodule.c -o spammodule.o'
result1 = shell(cmd1)
if result1.code != 0:
    print result1.errors()

cmd2 = 'gcc -shared spammodule.o -L/usr/local/lib -o spammodule.so'
result2 = shell(cmd2)
if result1.code != 0:
    print result1.errors()
