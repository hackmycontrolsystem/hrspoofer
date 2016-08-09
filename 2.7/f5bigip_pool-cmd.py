#!/usr/bin/python

print "create ltm pool dind_nginx members add { ",
for octet in range(2,52):

   print "172.18.0.%s:80 " %octet,

print " } monitor http"
