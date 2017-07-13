#!/usr/bin/env python
from netaddr import IPNetwork

# constants
# vars set as default

iplist = []
ipp = []
i = 0
s = 0
m = 0
h = 0

class cnt()
	def counti():
		i = i + 1
	def counts():
		s = s + 1
	def countm():
		m = m + 1
	def counth():
		h = h + 1


list = ["192.168.1.0/24", "10.20.10.0/24", "10.20.50.0/24", "10.1.10.0/24"]

def ipspace(list):
	iip = []
	for xlist in list:
		for ip in IPNetwork(xlist):
			iip.append(ip)
	return iip

def calculator():
	ipll = len(ipspace(list))
	iplcount = ipll * 65535
	x = 0
	p = 0
	while x < int(iplcount):
		p = p + 1
		x = p ** 2
	return str(p), str(x)


calculator()

cnt.counti()
