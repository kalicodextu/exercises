#!/usr/bin/env python
# -*- coding:utf-8 -*-

#================================================================
#   
#   File Name：gevent_test02.py
#   Author   ：GaoZhiChao
#   Date     ：2017年12月07日
#   Desc     ：fetching data from a server asynchronously, the runtime of fetch() will differ
#              between requests given the load on the remote server.
#
#================================================================


import gevent.monkey
gevent.monkey.patch_socket()


import gevent
import urllib2
import simplejson as json


def fetch(pid):
    response  = urllib2.urlopen('http://json-time.appspot.com/time.json')
    resualt = response.read()
    json_result = json.load(result)
    datetime = json_resualt['datetime']

    print 'Process ', pid, datetime


def synchronous():
    for i in range(10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(10):
        threads.append(gevent.spawn(fetch, i))

    gevent.joinall(threads)


print 'synchronous:'
synchronous()

print 'asynchronous:'
asynchronous()
