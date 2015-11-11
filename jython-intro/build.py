from shell import shell
from os import path

def shellCmd(cmd):
    result = shell(cmd)
    if result.code != 0:
        print result.errors()
        exit(-1)

appName = 'Example'
shellCmd('javac %(name)s.java' % {'name': appName})
shellCmd('jar cf %(name)s.jar %(name)s.class' % {'name': appName})
pwd = path.dirname(path.realpath(__file__))
print 'Run this to finish setup:\n', 'export CLASSPATH=%(pwd)s/%(name)s.jar' % {'name': appName, 'pwd': pwd}