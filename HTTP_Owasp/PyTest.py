def HTTPJUNK1_1(url):
    try:
        sys.modules
    except Exception as nosys:
        import sys
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    try:
        url = urlparse.urlparse(url)
    except Exception as nourlparse:
        import urlparse
        url = urlparse.urlparse(url)
        pass
    try:
        PORT = 80				# default HTTP port
        if str(url).split(":")[1]:
            PORT = int(str(str(url).split(":")[2]).split("/")[0])
    except Exception as noportgiven:
        pass
    try:
        CRLF = "\r\n\r\n"	# set CRLF for ease of readability
        HOST = url.netloc	# The remote host
    except Exceptions as nohost:
        print "URL is in an invalid format"
        sys.exit(0)
    try:
        path = url.path
        if path == "":
            path = "/"
    except Exception as nopath:
        print "\t[-] URL is in an invalid format"
        sys.exit(0)
    try:
        s.settimeout(5)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((HOST, PORT))
        s.send("JUNK %s HTTP/1.1%sHost: %s%s" % (path, CRLF, HOST, CRLF))
    except Exception as noconnect:
        print "\t[-] No connection could be established %s" % (noconnect)
        pass
    try:
        data = ''
        while True:
            sr = s.recv(1024)
            if not sr:
                break
            data += sr
        s.shutdown(1)
        s.close()
        return data
    except Exception as noread:
        print "No data was recieved %s" % (noread)
        pass


def HTTPJUNK1_0(url):
    try:
        sys.modules
    except Exception as nosys:
        import sys
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    try:
        url = urlparse.urlparse(url)
    except Exception as nourlparse:
        import urlparse
        url = urlparse.urlparse(url)
        pass
    try:
        PORT = 80				# default HTTP port
        if str(url).split(":")[1]:
            PORT = int(str(str(url).split(":")[2]).split("/")[0])
    except Exception as noportgiven:
        pass
    try:
        CRLF = "\r\n\r\n"	# set CRLF for ease of readability
        HOST = url.netloc	# The remote host
    except Exceptions as nohost:
        print "URL is in an invalid format"
        sys.exit(0)
    try:
        path = url.path
        if path == "":
            path = "/"
    except Exception as nopath:
        print "\t[-] URL is in an invalid format"
        sys.exit(0)
    try:
        s.settimeout(5)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((HOST, PORT))
        s.send("JUNK %s HTTP/1.0%s" % (path, CRLF))
    except Exception as noconnect:
        print "\t[-] No connection could be established %s" % (noconnect)
        pass
    try:
        data = ''
        while True:
            sr = s.recv(1024)
            if not sr:
                break
            data += sr
        s.shutdown(1)
        s.close()
        return data
    except Exception as noread:
        print "No data was recieved %s" % (noread)
        pass


def HTTPGET1_0(url):
    try:
        sys.modules
    except Exception as nosys:
        import sys
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    try:
        url = urlparse.urlparse(url)
    except Exception as nourlparse:
        import urlparse
        url = urlparse.urlparse(url)
        pass
    try:
        PORT = 80				# default HTTP port
        if str(url).split(":")[1]:
            PORT = int(str(str(url).split(":")[2]).split("/")[0])
    except Exception as noportgiven:
        pass
    try:
        CRLF = "\r\n\r\n"	# set CRLF for ease of readability
        HOST = url.netloc	# The remote host
    except Exceptions as nohost:
        print "URL is in an invalid format"
        sys.exit(0)
    try:
        path = url.path
        if path == "":
            path = "/"
    except Exception as nopath:
        print "\t[-] URL is in an invalid format"
        sys.exit(0)
    try:
        s.settimeout(5)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((HOST, PORT))
        s.send("GET %s HTTP/1.0%s" % (path, CRLF))
    except Exception as noconnect:
        print "\t[-] No connection could be established %s" % (noconnect)
        pass
    try:
        data = ''
        while True:
            sr = s.recv(1024)
            if not sr:
                break
            data += sr
        s.shutdown(1)
        s.close()
        return data
    except Exception as noread:
        print "No data was recieved %s" % (noread)
        pass


def HTTPGET1_1(url):
    try:
        sys.modules
    except Exception as nosys:
        import sys
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    try:
        url = urlparse.urlparse(url)
    except Exception as nourlparse:
        import urlparse
        url = urlparse.urlparse(url)
        pass
    try:
        PORT = 80         # default HTTP port
        if str(url).split(":")[1]:
            PORT = int(str(str(url).split(":")[2]).split("/")[0])
    except Exception as noportgiven:
        pass
    try:
        CRLF = "\r\n\r\n"	# set CRLF for ease of readability
        HOST = url.netloc	# The remote host
    except Exceptions as nohost:
        print "URL is in an invalid format"
        sys.exit(0)
    try:
        path = url.path
        if path == "":
            path = "/"
    except Exception as nopath:
        print "\t[-] URL is in an invalid format"
        sys.exit(0)
    try:
        s.settimeout(5)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((HOST, PORT))
        s.send("GET %s HTTP/1.1%sHost: %s%s" % (path, CRLF, HOST, CRLF))
    except Exception as noconnect:
        print "\t[-] No connection could be established %s" % (noconnect)
        pass
    try:
        data = ''
        while True:
            sr = s.recv(1024)
            if not sr:
                break
            data += sr
        s.shutdown(1)
        s.close()
        return data
    except Exception as noread:
        print "No data was recieved %s" % (noread)
        pass


def HTTPSGET1_1(url):
    try:
        sys.modules
    except Exception as nosys:
        import sys
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    try:
        ss = ssl.wrap_socket(s, 
                ca_certs='/usr/lib/python2.7/dist-packages/certifi/cacert.pem', 
                cert_reqs=ssl.CERT_REQUIRED)
    except Exception as nossl:
        import ssl
        ss = ssl.wrap_socket(s, 
                ca_certs='/usr/lib/python2.7/dist-packages/certifi/cacert.pem', 
                cert_reqs=ssl.CERT_REQUIRED)
        pass
    try:
        url = urlparse.urlparse(url)
    except Exception as nourlparse:
        import urlparse
        url = urlparse.urlparse(url)
        pass
    try:
        CRLF = "\r\n\r\n"	# set CRLF for ease of readability
        HOST = url.netloc	# The remote host
    except Exceptions as nohost:
        print "URL is in an invalid format"
        sys.exit(0)
    try:
        path = url.path
        if path == "":
            path = "/"
    except Exception as nopath:
        print "\t[-] URL is in an invalid format"
        sys.exit(0)
    try:
        PORT = 443         # default HTTPS port
        if str(url).split(":")[1]:
            PORT = int(str(str(url).split(":")[2]).split("/")[0])
    except Exception as noportgiven:
        pass
    try:
        s.settimeout(5)
        ss = ssl.wrap_socket(s, 
                ca_certs='/usr/lib/python2.7/dist-packages/certifi/cacert.pem', 
                cert_reqs=ssl.CERT_REQUIRED)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ss.connect((HOST, PORT))
        ss.write("GET %s HTTP/1.1%sHost: %s%s" % (path, CRLF, HOST, CRLF))
    except Exception as noconnect:
        print "\t[-] No connection could be established %s" % (noconnect)
        pass
    try:	
        data = ''
        while True:
            sr = ss.read(1024)
            if not sr:
                break
            data += sr
        ss.shutdown(1)
        ss.close()
        return data
    except Exception as noread:
        print "No data was recieved %s" % (noread)
        pass

def HTTPSGET1_0(url):
    try:
        sys.modules
    except Exception as nosys:
        import sys
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    try:
        ss = ssl.wrap_socket(s, 
                ca_certs='/usr/lib/python2.7/dist-packages/certifi/cacert.pem', 
                cert_reqs=ssl.CERT_REQUIRED)
    except Exception as nossl:
        import ssl
        ss = ssl.wrap_socket(s, 
                ca_certs='/usr/lib/python2.7/dist-packages/certifi/cacert.pem', 
                cert_reqs=ssl.CERT_REQUIRED)
        pass
    try:
        url = urlparse.urlparse(url)
    except Exception as nourlparse:
        import urlparse
        url = urlparse.urlparse(url)
        pass
    try:
        CRLF = "\r\n\r\n"	# set CRLF for ease of readability
        HOST = url.netloc	# The remote host
    except Exceptions as nohost:
        print "URL is in an invalid format"
        sys.exit(0)
    try:
        path = url.path
        if path == "":
            path = "/"
    except Exception as nopath:
        print "\t[-] URL is in an invalid format"
        sys.exit(0)
    try:
        PORT = 443         # default HTTPS port
        if str(url).split(":")[1]:
            PORT = int(str(str(url).split(":")[2]).split("/")[0])
    except Exception as noportgiven:
        pass
    try:
        s.settimeout(5)
        ss = ssl.wrap_socket(s, 
                ca_certs='/usr/lib/python2.7/dist-packages/certifi/cacert.pem', 
                cert_reqs=ssl.CERT_REQUIRED)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ss.connect((HOST, PORT))
        ss.write("GET %s HTTP/1.0%s" % (path, CRLF))
    except Exception as noconnect:
        print "\t[-] No connection could be established %s" % (noconnect)
        pass
    try:	
        data = ''
        while True:
            sr = ss.read(1024)
            if not sr:
                break
            data += sr
        ss.shutdown(1)
        ss.close()
        return data
    except Exception as noread:
        print "No data was recieved %s" % (noread)
        pass


HTTPSGET1_1('https://google.com')
HTTPSGET1_0('https://google.com')
HTTPGET1_0('http://www.google.com')
HTTPGET1_1('http://www.google.com')
HTTPJUNK1_0('http://10.1.10.1')
HTTPJUNK1_1('http://10.1.10.1')

def checksys():
    try:
        sys.modules
    except Exception as nosys:
        import sys
        pass

def checkurl(URL):
    try:
        URL = urlparse.urlparse(URL)
    except Exception as nourlparse:
        import urlparse
        URL = urlparse.urlparse(URL)
        pass
    return URL

def parseport(URL):
    try:
        SCHEMA = str(URL.scheme).lower()
        try:
            if str(SCHEMA) == "http":
                PORT=int('80')
                if str(URL.netloc).split(":")[1]:
                    PORT = int(str(URL.netloc).split(":")[1])
            if str(SCHEMA) == "https":
                PORT=int('443')
                if str(URL.netloc).split(":")[1]:
                    PORT = int(str(URL.netloc).split(":")[1])
        except Exception:
            pass
    except Exception as noschema:
        print "\t[-] URL PORT is in an invalid format:\n\t\t[?] %s" % (noschema)
    return PORT

def parsehost(URL):
    try:
        HOST = URL.netloc
    except Exception as nohost:
        print "\t[-] URL HOST is in an invalid format:\n\t\t[?] %s" % (nohost)
    return HOST

def parsepath(URL):
    try:
        PATH = URL.path
        if PATH == "":
            PATH = "/"
    except Exception as nopath:
        print "\t[-] URL PATH is in an invalid format:\n\t\t[?] %s" % (nopath)
    return PATH

def makeattack():
    ATTACK = {}
    ATTACK['SEND'] = []
    ATTACK['RECIEVE'] = []
    return ATTACK

def VERBTAMP1_1(url):
    CRLF = "\r\n\r\n"
    NL = "\n"
    VERBS = ['PUT', 'DELETE', 'GET', 'PATCH', 'POST', 'JUNK']
    checksys()
    URL=checkurl(url)
    SCHEMA=parseschema(URL)
    HOST=parsehost(URL)
    PORT=parseport(URL)
    PATH=parsepath(URL)
    try:
        try:
            ATTACK=makeattack()
            for VERB in VERBS:
                PAYLOAD = ''
                ATTACKSTRING="%s %s HTTP/1.1\nHost: %s\nConnection: keep-alive\nUser-Agent: Testing\nUpgrade-Insecure-Requests:1\nAccept: *.*%s" % (VERB, PATH, HOST, CRLF)
                ATTACK['SEND'].append(ATTACKSTRING)
                if SCHEMA == 'http':
                    AS=gensock(HOST, PORT, ATTACKSTRING)
                else:
                    AS=gensecsock(HOST, PORT, ATTACKSTRING)
                ATTACK['RECIEVE'].append(AS)
        except Exception:
            pass
    except Exception as noconnect:
        print "\t[-] VT No connection could be established:\n\t\t[?] %s" % (noconnect)
        pass
    return ATTACK

VERBTAMP1_1('https://google.com')

def VERBTAMP1_0(url):
    verbs = ['PUT','DELETE','GET','PATCH','POST']
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        pass
    try:
        sys.modules
    except Exception as nosys:
        import sys
        pass
    try:
        url = urlparse.urlparse(url)
    except Exception as nourlparse:
        import urlparse
        url = urlparse.urlparse(url)
        pass
    try:
        PORT = 80         # default HTTP port
        if str(url).split(":")[1]:
            PORT = int(str(str(url).split(":")[2]).split("/")[0])
    except Exception as noportgiven:
        pass
    try:
        CRLF = "\r\n\r\n"	# set CRLF for ease of readability
        HOST = url.netloc	# The remote host
    except Exception as nohost:
        print "URL is in an invalid format:\n\t\t[?] %s" %(nohost)
        sys.exit(0)
    try:
        path = url.path
        if path == "":
            path = "/"
    except Exception as nopath:
        print "\t[-] URL is in an invalid format:\n\t\t[?] %s" % (nopath)
        sys.exit(0)
    try:
        ATTACK = {}
        ATTACK['SEND'] = []
        ATTACK['RECIEVE'] = []
        for verb in verbs:
            ATTACKSTRING = "%s %s HTTP/1.0%s" % (verb, path, CRLF)
            ATTACK['SEND'].append(ATTACKSTRING)

            ATTACK['RECIEVE'].append(data)
    except Exception as noconnect:
        print "\t[-] No connection could be established:\n\t\t[?] %s" % (noconnect)
        pass
    return ATTACK


def gensecsock(HOST, PORT, STRING):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
    s.settimeout(5)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        ss = ssl.wrap_socket(s, 
                ca_certs='/usr/lib/python2.7/dist-packages/certifi/cacert.pem',cert_reqs=ssl.CERT_REQUIRED)
    except Exception as nossl:
        import ssl
        ss = ssl.wrap_socket(s, 
                ca_certs='/usr/lib/python2.7/dist-packages/certifi/cacert.pem',cert_reqs=ssl.CERT_REQUIRED)
        pass
    ss.connect((HOST, PORT))
    ss.write(STRING)
    DATA = ''
    while True:
        sr = ss.read(1024)
        if not sr:
            break
        DATA += sr
    ss.shutdown(1)
    ss.close()
    return DATA

def gensock(HOST, PORT, STRING):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as nosocket:
        import socket
        pass
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT))
    s.send(STRING)
    DATA = ''
    while True:
        sr = s.recv(1024)
        if not sr:
            break
        DATA += sr
    s.shutdown(1)
    s.close()
    return DATA

def vt1_0parse(url):
    A=VERBTAMP1_0(url)
    RL=len(A['RECIEVE'])
    SL=len(A['SEND'])
    for x in xrange(SL):
        R=A['RECIEVE'][x]
        S=A['SEND'][x]
        print "[-] Sent:---------------------------------------------------\n\n%s" % (S)
        print "[-] Recieved:-----------------------------------------------\n\n%s" % (R)

vt1_0parse('http://10.1.10.1')


def vt1_1parse(url):
    A=VERBTAMP1_1(url)
    RL=len(A['RECIEVE'])
    SL=len(A['SEND'])
    for x in xrange(SL):
        R=A['RECIEVE'][x]
        S=A['SEND'][x]
        print "[-] Sent:---------------------------------------------------\n\n%s" % (S)
        print "[-] Recieved:-----------------------------------------------\n\n%s" % (R)

vt1_1parse('http://10.1.10.1')
vt1_1parse('https://google.com')
