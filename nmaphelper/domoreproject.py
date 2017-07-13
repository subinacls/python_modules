# this script came about due to testing and other essentials which were highly time sensitive 
# needed a way to do more with less, initial bash scripts
# for x in $(seq 1 255); do 
#   nmap -sn 192.20.$x.0 -v -n | tee testing_192.20.$x.0_pingscan;
#   nmap -Pn -R 192.20.$x.0 -v -n | tee testing_192.20.$x.0_all_host_resolve ;
#   #nmap -sS --disable-arp-ping 192.20.$x.0 -v -n | tee testing_192.20.`echo $x`.0_arpscan;
# done
# sd () { grep Discovered `pwd`/* | sed -r "s/(.*) on (.*)/\2/g" | sort -u | sort -n -t "." -k3 | wc -l; }
# 
import os
import sys
import time
import subprocess
import shlex
from netaddr import *
import multiprocessing as mp
import __builtin__ as bi

bi.fna = "CPA"
tports = 1000

class inital():
 def __init__(self):
  pass
 def takeactions(self):
  try:
   # gather system information
   cpuc = mp.cpu_count()
  except Exception as nomcpu:
   print "Are you even a computer bro ?"
   pass
  try:  # take user info
   bi.iprange = "96.66.91.148-158" #sys.argv[1]
   #exclusion = sys.argv[2]
  except Exception as nv:
   print " Supply a Variable, read the source"
   sys.exit()
  '''
  bi.eports = []
  try:  # two phases to identify - filetype or supplied string
   try:  # read file
    with open(exclusion, 'r').readlines() as elist:
     for xelist in elist:
      bi.eports.append(xelist)
   except Exception as notafile:
    for xelist in exclusion.split(","):
     bi.eports.append(xelist)
  except Exception as Elist:
   print "The app failed on parsing the exclusions list"
  '''
  # do some work now ....
  # test ports to exclude-ports
  bi.eports = [1234,4321]
  
 def sactions(self):
  try:
   bi.eps = ",".join(map(str,bi.eports))  # make string from list
   try:
    bi.net = str(bi.iprange).split("/")[0]  # split user var 1  [network]
    bi.cidr = str(bi.iprange).split("/")[1]  # split user var 1 [cidr]
    bi.iscidr = 1
   except:
    bi.net = str(bi.iprange).split("-")[0]  # split user var 1  [network]
    bi.cidr = str(bi.iprange).split("-")[1]  # split user var 1 [cidr]
    bi.iscidr = 0
  except Exception as sactionfail:
   pass


inital().takeactions()  # initialize the application, take user variables
inital().sactions()  # static actions on user supplied variables


class havenone:
 def __init__(self):
  pass
 # define subnets from CIDR
 def ipworks(self):
  ip = IPNetwork(iprange)  # take user var input for IP Range
  subnets = list(ip.subnet(28))  # default cidr range to make class B networks more managable
  print "\t[-] Total subnets to test:\t%s" %(len(subnets))  # diagnostic
  print "\t[-] Total IP addr to test:\t%s" % (len(subnets) * 256)  # diagnostic
#havenone().ipworks()  # diagnostic

class hostdisco:
 def __init__(self):
  self.fna	= bi.fna
  self.cird	= bi.cidr
  self.net	= bi.net
  self.eps	= bi.eps
  self.ipr	= bi.iprange
  pass
 # attempt SYN port discovery on target networks - top ports
 def makefilename(self, scantype):
  if bi.cidr == 1:
   bi.fna = "1"# % (scantype, bi.net, bi.cidr)
  else:
   bi.fna = "12345678901234567890123456789012345678901234567890"# % (scantype, bi.net, bi.cidr)
 def tpsyn(self):
  self.makefilename("TCP_SYN_ALL_PORT")
  cmd = "/usr/bin/nmap %s -sS -n -v --open -p 0-65535 --exclude-ports=%s -T5 --min-parallelism=90 -oA %s" % (bi.iprange, bi.eps, bi.fna)
  arg = shlex.split(cmd) 
  output = subprocess.check_output(arg)
  print output
 # attempt FULL CONNECT port discovery on target networks - all ports
 def tpcon(self):
  try:
   self.makefilename("TCP_CON_ALL_PORT")
   cmd = "/usr/bin/nmap %s -sC -n -v --open -p 0-65535 --exclude-ports=%s -T5 --min-parallelism=90 -oA %s" % (bi.iprange, bi.eps, bi.fna)
   arg = shlex.split(cmd)
   output = subprocess.check_output(cmd)
   print output
  except Exception as e:
   print e

hostdisco().tpsyn()  # diagnostic, top_ports SYN
hostdisco().tpcon()  # diagnostic, top-ports CONNECT

class deepscan:
 def __init__(self):
  pass
 # attempt all TCP ports discovery on target networks - top ports
 def apcon(self):
  cmd = "/usr/bin/nmap %s -sCT -n -v --open -p- --exclude-ports=%s -T5 --min-parallelism=90 | tee al_TCP_PORTS_%s-%s" % (iprange, eps, net, cidr)
  arg = shlex.split(cmd)
  output = subprocess.check_output(cmd)

deepscan().apcon()  # disgnostic, all ports TCP

inital().takeactions()  # initialize the application, take user variables
inital().sactions()  # static actions on user supplied variables
havenone().ipworks()  # break the cird into smaller chunks
