import os
import requests
from datetime import datetime

TOKEN_NOTIF = ""
TOKEN_CONTROL = ""
CHAT_ID = ''
MIN = 60
MAX = 85

def sensor():
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1_bus_master_1':
			ds18b20 = i
	return ds18b20

def read(ds18b20):
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	tfile = open(location)
	text = tfile.read()	
	tfile.close()
	secondline = text.split("\n")[1]
	temp_data = secondline.split(" ")[9]
	temp = float(temp_data[2:])
	celsius = temp/1000
	faran = (celsius * 1.8) + 32
	return celsius, faran

def reply_notif(text):
    url = f'https://api.telegram.org/bot{TOKEN_NOTIF}/sendMessage'
    payload = {
                'chat_id': CHAT_ID,
                'text': text
    }
    r = requests.post(url,json=payload)


last_send = datetime.now()
def reply_control(text):
	global last_send	
	# send msgs only in 30 seconds interval
	curr = datetime.now()
	if (curr - last_send).seconds < 30:
		return
	
	url = f'https://api.telegram.org/bot{TOKEN_CONTROL}/sendMessage'
	payload = {
		'chat_id': CHAT_ID,
		'text': text
	}
	r = requests.post(url,json=payload)
	last_send = curr


def crosses_threshold(f):
	return f < MIN or f > MAX


def loop(ds18b20):
	while True:
		if read(ds18b20) != None:
			c, f = read(ds18b20)
			print("Current temperature: %0.3f C, %0.3f F" % (c,f))
			reply_notif("Current temperature: %0.3f C, %0.3f F" % (c,f))
			if crosses_threshold(f):
				reply_control("Current temperature crossed threshold: %0.3f C, %0.3f F" % (c,f))

def kill():
	quit()

if __name__ == "__main__":
	try:
		s_no = sensor()
		loop(s_no)
	except KeyboardInterrupt:
		kill()
