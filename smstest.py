import os

x = "E77A0EX6HXFYL0QU"
target = "1234567890"
count = "1"
subject = "testing this shit"
msg = "yeah boy!"
choice = "vtext.com"
upload = "/var/lib/veil-evasion/go/doc/gopher/pencil/gopherrunning.jpg"


cmd = "sudo su " + str(x) + " -c 'echo " +str(msg) + " | mail -s " + str(subject) + " " + str(target) + "@" + str(choice) + "'"

os.popen("sudo su " + str(x) + " -c 'echo " +str(msg) + " | mutt -s " + str(subject) + " " + str(target) + "@" + str(choice) + " -a'").readlines()



"sudo su " + str(x) + " -c \"whoami && echo '" +str(msg) + "' | mail -s '" + str(subject) + "' '" + str(target) + "@" + str(choice) + "' && exit\""
