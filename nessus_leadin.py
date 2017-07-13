#!/usr/bin/env python
# Nessus CSV Python Parser
#
# Makes directories for services, and each cotnaining a TARGET file in {IP:PORT} format
# Useful to parse out service specific attacks to gather information from suchs as banner images.

from os import popen as p
from sys import argv as a
import csv

def readfile():
	with open('r.csv', 'rb') as csvread:  # change this to take argument
		reader = csv.reader(csvread)
		csvin = map(tuple, reader)
		return csvin

nlist = readfile()

pdir = str("projecttest").strip()

def project_dir(pdir):
	if not os.path.exists(pdir):
		os.makedirs(pdir)

project_dir(pdir)

def writelistout(pdir, filename, listname):
	project_dir(pdir)
	with open(str(pdir)+"/"+str(filename), "w+") as ssrout:
		for xline in listname:
			#print xline
			ssrout.write(str(xline).strip()+"\n")
			#print xline

def pluginidlist():
	# makes a list plugginids
	fname = "Pluggin_ID_Results.txt"
	plist = []
	for x in xrange(1,len(nlist)):
		pline = "%s" %(str(nlist[x][0]))
		plist.append(pline)
		plist = sorted(set((plist)))
		#print pline
	if len(plist) == 0:
		pass
	else:
		writelistout(str(pdir)+"/PlugginID/", fname, plist)
	plist = []


pluginidlist()


def fqdnlist():
	# makes a list of ports identified through nessus ID 11219
	# TCP SYN Port Scan identified as Open
	fname = "FQDN_Results.txt"
	flist = []
	for x in range(len(nlist)):
		if str(nlist[x][0]) == "12053":
			fline = "%s:%s" %(str(nlist[x][4]),str(nlist[x][12]).split(" ")[-1])
			flist.append(fline)
			#print fline
	if len(flist) == 0:
		pass
	else:
		writelistout(str(pdir)+"/FQDN/", fname, flist)
	flist = []


fqdnlist()


def synscanlist():
	# makes a list of ports identified through nessus ID 11219
	# TCP SYN Port Scan identified as Open
	fname = "SYN_Scanner_Results.txt"
	slist = []
	risk = "Informational"
	for x in range(len(nlist)):
		if str(nlist[x][0]) == "11219":
			aline = "%s:%s" %(str(nlist[x][4]),str(nlist[x][6]))
			slist.append(aline)
			#print aline
	if len(slist) == 0:
		pass
	else:
		dirname = "%s/$sRisk/" (pdir, risk)
		writelistout(dirname, fname, slist)
	slist = []


synscanlist()

def getinfolist():
	# makes a list of Low risk rating all IDs 
	fname = "Info_Risk_Results.txt"
	ilist = []
	iwrite = []
	risk = "Informational"
	for x in range(len(nlist)):
		if str(nlist[x][3]) == "None":
			iline = "%s - %s:%s \"%s\"" %(str(nlist[x][0]),str(nlist[x][4]),str(nlist[x][6]), str(nlist[x][7]))
			ilist.append(iline)
			iwrite.append(nlist[x])
			#print iline
	if len(ilist) == 0:
		pass
	else:
		dirname = "%s/$sRisk/" (pdir, risk)
		writelistout(dirname, fname, ilist)
	for z in iwrite:
		Validation(risk, z)
	ilist = []


getinfolist()


def getlowlist():
	# makes a list of Low risk rating all IDs 
	fname = "Low_Risk_Results.txt"
	llist = []
	lwrite = []
	risk = "Low"
	for x in range(len(nlist)):
		if str(nlist[x][3]) == "Low":
			lline = "%s - %s:%s \"%s\"" %(str(nlist[x][0]),str(nlist[x][4]),str(nlist[x][6]), str(nlist[x][7]))
			llist.append(lline)
			lwrite.append(str(nlist[x:]))
			#print aline
	if len(llist) == 0:
		pass
	else:
		dirname = "%s/%sRisk/" % (str(pdir), risk)
		writelistout(dirname, fname, llist)
	Validation(risk, lwrite)
	llist = []


getlowlist()

def getmedlist():
	# makes a list of Low risk rating all IDs 
	fname = "Medium_Risk_Results.txt"
	mlist = []
	mwrite = []
	risk = "Medium"
	for x in range(len(nlist)):
		if str(nlist[x][3]) == "Medium":
			mline = "%s - %s:%s \"%s\"" %(str(nlist[x][0]),str(nlist[x][4]),str(nlist[x][6]), str(nlist[x][7]))
			mlist.append(mline)
			mwrite.append(str(nlist[x]))
			##print mline
	if len(mlist) == 0:
		pass
	else:
		dirname = "%s/$sRisk/" (pdir, risk)
		writelistout(dirname, fname, mlist)
	sshcbcmode(risk, mwrite)
	mlist = []


getmedlist()

def gethighlist():
	# makes a list of Low risk rating all IDs 
	fname = "High_Risk_Results.txt"
	hlist = []
	hwrite = []
	risk = "High"
	for x in range(len(nlist)):
		if str(nlist[x][3]) == "High":
			hline = "%s - %s:%s \"%s\"" %(str(nlist[x][0]),str(nlist[x][4]),str(nlist[x][6]), str(nlist[x][7]))
			hlist.append(hline)
			hwrite.append(nlist[x])
			##print hline
	if len(hlist) == 0:
		pass
	else:
		dirname = "%s/$sRisk/" (pdir, risk)
		writelistout(dirname, fname, hlist)
	Validation(risk, hwrite)
	hlist = []


gethighlist()

def getcriticallist():
	# makes a list of Low risk rating all IDs 
	fname = "Critical_Risk_Results.txt"
	clist = []
	cwrite = []
	risk = "Critical"
	for x in range(len(nlist)):
		if str(nlist[x][3]) == "Critical":
			cline = "%s - %s:%s \"%s\"" %(str(nlist[x][0]),str(nlist[x][4]),str(nlist[x][6]), str(nlist[x][7]))
			clist.append(cline)
			cwrite.append(nlist[x])
			#print cline
	if len(clist) == 0:
		pass
	else:
		dirname = "%s/$sRisk/" (pdir, risk)
		writelistout(dirname, fname, clist)
	Validation(risk, cwrite)
	clist = []
	cwrite = []


getcriticallist()


def sshcbcmode(risk, targets):
	try:
		# 70658 - 216.200.165.1:2022 "SSH Server CBC Mode Ciphers Enabled"
		fname = "SSH_Weakness_Enumeration_Results.txt"
		print fname
		for target in targets:
			print str(str(target).split(",")[0].split("(")[1])
			if int(str(target).split(",")[0].split("(")[1]).split("'")[0:2] in [70658, 71049, 86328]:
				print target
				v_routine = "nmap -sV -v -Pn --script ssh2-enum-algos %s -p %s" % (str(target).split(",")[4],str(target).split(",")[6])
				ssh_cbc_test = os.popen(v_routine).readlines()
				if ssh_cbc_test:
					dirname = "%s/%sRisk/" % (pdir, risk)
					print ssh_cbc_test  #writedumpout(dirname, fname, ssh_cbc_test)
				else:
					pass
			else:
				pass
	except Exception as e:
		print e


getlowlist()

def Validation(risk, targets):
	sshcbcmode(risk, targets)
