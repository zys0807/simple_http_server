#!/usr/bin/env python
# coding=utf-8
# 
import threading
from time import ctime,sleep
import time
import json
import time
import httplib, urllib
import sys
import pycurl
from StringIO import StringIO

#ip = "10.10.40.107"
#ip = "123.59.127.126"
ip = "192.168.116.128"

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, "http://" + ip + ":7788/in_room")
c.setopt(pycurl.HTTPHEADER, ['Content-type: application/json'])
c.setopt(pycurl.HTTPHEADER, ['Proxy-Connection: Proxy-Connection'])

#devnull = open('/dev/null', 'w')
#c.setopt(pycurl.WRITEFUNCTION, devnull.write)

def write_data(return_data):
    print return_data
    pass
c.setopt(pycurl.WRITEFUNCTION, write_data)

for x in xrange(0, 11):
    #print "x: %d" % x
    userid = str(x)
    tmp1 = { "cmd": "XY_ROOM_REQUEST_IN", "roomid": "roomid", "userid": userid }

    c.setopt(c.POSTFIELDS, json.dumps(tmp1))
    time1 =time.time()
    c.perform()
    time2 =time.time()
    print "%f" % (time2-time1)
    #body = buffer.getvalue()
    #print body
c.close()
