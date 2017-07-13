import os
import __builtin__ as bi

# defaults

bi.termlist = {}


# Defined functions
def startscreen(session_name):
	scmd = "/usr/bin/screen -dmS %s\n" % (session_name)
	return scmd


def addterm(termlist, session_name, NewCMD):
	print "Session name: %s" % (session_name)
	try:  # check if screen session name is already tracked
		if session_name in bi.termlist.keys():
			print "Session name Key Exists"
		else:
			bi.termlist[session_name] = {}
	except Exception as failsessioncheck:
		print "Failed Session check: %s" % (failsessioncheck)
		pass  # testing only, usually fail and exit
	try:
		if 'term_count' in bi.termlist[session_name].keys():
			bi.termlist[session_name]['term_count'] = int(bi.termlist[session_name]['term_count']) + 1
			tcount = bi.termlist[session_name]['term_count']
			print "Term Count Key Exists"
			print "Term count is: %s" % (tcount)
		else:
			bi.termlist[session_name]['term_count'] = 0
			tcount = bi.termlist[session_name]['term_count']
			print "Added counter to %s" % (session_name)
	except Exception as failtermcount:
		print "Failed Terminal Count check: %s" % (failtermcount)
		pass  # testing only, usually fail and exit
	try:
		if 'created' in bi.termlist[session_name].keys():
			startscreen(session_name)
			acmd = "/usr/bin/screen -S %s -p %d -X screen %s\n" % (session_name, tcount, NewCMD)
		else:
			acmd = "/usr/bin/screen -DmS %s &" % (session_name)
			bi.termlist[session_name]['created'] = '1'
		try:
			if 'cmd_log' in bi.termlist[session_name].keys():
				bi.termlist[session_name]['cmd_log'].append(acmd)
				print "Cmd log Key Exists"
				print "Cmd log entry: %s" % ("\n[-] " + acmd + "\n")
			else:
				bi.termlist[session_name]['cmd_log'] = []
				bi.termlist[session_name]['cmd_log'].append(acmd)
				print "Cmd log entry: %s" % ("\n[-] " + acmd + "\n")
		except Exception as failecmdlogcheck:
			print "Failed Cmd Log Count check: %s" % (failecmdlogcheck)
			pass  # testing only, usually fail and exit
	except Exception as failedall:
		print "failed at %s" % (failedall)
	return acmd

def appendterm(termlist, session_name, NewCMD):
	tcount = termlist[session_name]['term_count']
	aterm = "/usr/bin/screen -S %s -X stuff %s\n" % (session_name, NewCMD)
	return aterm
 
def NewShell(session_name):
 return 0

def RunCMD(DoCMD):
 os.popen(DoCMD)

def screenlist():
	a = os.popen('screen -list | grep -v Socket | grep -E "\t" | tr -d "\t" | cut -d"(" -f1').readlines()
	for x in a:
		print x.strip("\n")

session_name = "new"
NewCMD = 'cat /root/.ssh/known_hosts'
#RunCMD(startscreen(session_name))
RunCMD(addterm(bi.termlist, session_name, NewCMD))
RunCMD(addterm(bi.termlist, session_name, 'ls -asl'))

def wipeup():
 os.popen("/usr/bin/screen -wipe")

