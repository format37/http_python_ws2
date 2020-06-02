from requests.auth import HTTPBasicAuth
import requests
import json

with open('auth.login','r') as file:
	login=file.read().replace('\n', '')
	file.close()
with open('auth.pass','r') as file:
	password=file.read().replace('\n', '')
	file.close()

auth	= HTTPBasicAuth(login, password)
url		= "http://10.2.4.141/CRM/hs/createOrder"
params = {
	'token': 		'0',
	'shopId': 		'1',
	'specialistId':	'2',
	'serviceId':	'3',
	'dateAndTime':	'4',
	'clientName':	'5',
	'clientPhone':	'6',
	'clientEmail':	'7',
	'price':		'8',
	'orderParameters': [
		{'type':'comment', 			'value':'a'},
		{'type':'address', 			'value':'b'},
		{'type':'numberofpeople',	'value':1},
		{'type':'floorArea',		'value':47},
	],
}

r = requests.post(url, json=json.dumps(params), auth=auth)

#print(r.status_code, r.reason)
print(r.text)
