def validate_devices():
	# ensures no tampering with given directories
	# uses known signatures of files and devices
  # takes  JSON dump of the values of remote system
	import netifaces ## might need to pip this module on your system
  global validdevs
	validdevs = {}
	# get system UUID
	uuid=os.popen('dmidecode | grep UUID').readlines()
	uuid=str(uuid[0]).split("\t")[1].split(" ")[1].strip()
	validdevs['UUID'] = uuid
	# get mac addresses
	validdevs['MACS'] = {}
	netifaces.interfaces()
	for x in netifaces.interfaces():
		if x == "lo":
			continue
		else:
			validdevs['MACS'][str(x)] = str(netifaces.ifaddresses(x)[netifaces.AF_LINK][0]['addr'])
	# get usb devices
	usbdevids=os.popen('lsusb | cut -d" " -f6-').readlines()
	validdevs['USB'] = {}
	for xudevs in usbdevids:
		xudevn = str(xudevs).split(" ")[0].strip()
		xudevns = " ".join(str(xudevs).split(" ")[1::])
		validdevs['USB'][xudevn] = str(xudevns).strip()
	# get tar hash value of config dir and files
	# used to identify changes on mission critical system files
	validdevs['FILE'] = {}
	loclist = ["/root/observer/config","/etc/init.d","/root/.ssh"]
	for loc in loclist:
		fhash=os.popen('tar -cf - '+loc+' 2>/dev/null | sha256sum | cut -d " " -f1').readlines()
		validdevs['FILE'][loc] = str(fhash[0]).strip()
	return validdevs
