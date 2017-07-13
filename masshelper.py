#!/usr/bin.env python
# take top ports list and iterates it with massscan
# topscan.py ./top_ports.txt ./target_ranges.txt
# not finished working on this - 
import os
import sys
import threading
from queue import Queue
import time


with open(sys.argv[1]) as plist:
 rplines = plist.readlines()
with open(sys.argv[2]) as tlist:
 rtlines = tlist.readlines()

for p in rplines:
 for t in rtlines:
  outfile = 'massscan_%s_%s' % (t,p)
  cmd = 'massscan -sS -n -p %s $s > %s &' % (p,t, outfile)
  os.popen(cmd)

def exampleJob(worker):
    time.sleep(.5) # pretend to do some work.
    with print_lock:
        print(threading.current_thread().name,worker)
