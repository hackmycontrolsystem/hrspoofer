#!/usr/bin/python

from ipaddr import *

print "create ltm pool dind_nginx members add { ",
for ip in IPNetwork('10.10.0.0/26'):
   print "%s:80 " %ip,

print " } monitor http"
