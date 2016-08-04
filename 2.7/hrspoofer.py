#!/usr/bin/python

__author__ = "AJN (ajn.bin@gmail.com): cciethebeginning.wordpress.com"

import csv
import sys
import httplib
 
total_args = len(sys.argv)
if total_args != 4:
    print "\n"
    print "Usage: ./%s <destination host> <destination port> <file.csv>" %sys.argv[0]
    print "    destination host/port  : Web server virtual IP and port to test"
    print "    <file.csv>   : obtained using the script >>  gen_temp_ip.py << \n"
    sys.exit(1)

IP_DST=sys.argv[1]
PORT_DST=sys.argv[2]

with open('ip-port.csv') as ip_port_csvfile:
    reader = csv.reader(ip_port_csvfile, delimiter=',')
    for row in reader:
        IP_SRC=row[0]
        PORT_SRC=int(row[1])
        print "Sending request from ( %s , %s )" %(IP_SRC,PORT_SRC)
        try:
	  conn = httplib.HTTPConnection(host=IP_DST, port=PORT_DST, source_address=(IP_SRC,PORT_SRC),timeout=2)
	  conn.request("GET", "/")
	  res = conn.getresponse()
	  #print res.status, res.reason
        
        except:
          print "Unexpected error:", sys.exc_info()[0]      

