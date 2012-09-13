#!/usr/bin/python

import sys
import urllib
import urllib2

def read_message():
	while True:
		print "Type your message in one line:"
		msg = sys.stdin.readline().strip()
		if (len(msg) < 1):
			print "message too short"
			continue
		return msg

def read_recipient():
	while True:
		print "Enter recipient's GSM number:"
		gsm = sys.stdin.readline().strip()
		if (gsm.isdigit() and len(gsm) == 9):
			return gsm
		print "check your number"
		continue

def send_sms(gsm,msg):
	url	=	'https://sms.api.provider/script'
	values	=	{
			'un'	:	'username',
			'ps'	:	'apikey',
			'from'	:	'CENSORED',
			'to'	:	gsm,
			'm'	:	msg,
			'cc'	:	'386'
			}

	data = urllib.urlencode(values)
	req = urllib2.Request(url,data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page


def main():

	try:
		msg = read_message()
		gsm = read_recipient()
	except KeyboardInterrupt:
		print "CTRL+C caught... byebye"
		return 1

	print "Send? (yes/NO)"
	try:
		send = sys.stdin.readline()
	except KeyboardInterrupt:
		print "CTRL+C caught... byebye"
		return 1

	if (send.strip() == "yes"):
		print "sending..."
		return send_sms(gsm,msg)
	else:
		print "Aborted..."
	return 0
	

if __name__ == '__main__':
	main()
