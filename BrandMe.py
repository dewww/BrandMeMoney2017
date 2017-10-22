import bz2
import ui
from base64 import b64decode
import requests
import pprint
import time
import json

data = '''\
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
d99rmEvD7gjgFMRYtZ/8XckU4UJAzZHfeA
'''

# ———————————————————— 

pyui = bz2.decompress(b64decode(data))

pp = pprint.PrettyPrinter(indent=4)

def microtime(get_as_float = False) :
	if get_as_float:
		return time.time()
	else:
		return '%f %d' % math.modf(time.time())

def MODO(action='mint',arg1=None,arg2=None):
	#Key: uFiRj0L_RXG1b_BMlXeJA64dr1ySOexq
	#apiSecret: Bc-OMLe0dbtx_htHG7EzbrugiD_N5bsYZKClzki-cCDd2cbE6ERv1mhOwpW3y_NR

	#url = 'https://api.github.com/events'
	headers={}
	body=''

	#	method = 'GET'
	#url='https://api.sbx.gomo.do/api_v2/merchant/list'
	#url='https://api.sbx.gomo.do/api_v2/vault/get_type_list'
	
	if action=='mint':
		method = 'POST'
		url='https://api.sbx.gomo.do/api_v3/coin/mint'
	elif action=='add':
		method = 'POST'
		url='https://api.sbx.gomo.do/api_v2/vault/add'
	elif action=='register':
		method = 'POST'
		url='https://api.sbx.gomo.do/api_v2/people/register'

	#url='https://api.sbx.gomo.do/api_v3/coin/account_types'
	#url='https://api.sbx.gomo.do/api_v2/people/register'

	#headers = {'X-Modo-Date':str(timestamp), 'Authorization':'MOD0 key=uFiRj0L_RXG1b_BMlXeJA64dr1ySOexq','Content-Type':'application/x-www-form-urlencoded'}
	headers = {'Authorization':'MODO0 key=uFiRj0L_RXG1b_BMlXeJA64dr1ySOexq','Content-Type':'application/json'}

	if url.endswith('register') and arg1=='Shelley':
		body="""\
{"phone": 1234567890,"fname": "Shelley","lname": "Doe","email": "info@modopayments.com"}
""".encode('utf-8')
	if url.endswith('register') and arg1=='Dewayne':
		body="""\
{"phone": 2345678901,"fname": "Dewayne","lname": "Doe","email": "info@modopayments.com"}
""".encode('utf-8')
	elif url.endswith('add') and arg1=='Dewayne':
		body="""
{
  "items": [{
    "vault_type": "OPEN_CARD",
    "description": "vault/add a json_to_be_encrypted credit card",
    "json_to_be_encrypted": "{\\"pan\\":\\"5153648888888880\\",\\"exp_month\\":12,\\"exp_year\\":2020,\\"zip\\":\\"33333\\",\\"cvv\\":123}"
  }]
}
""".encode('utf-8')
	elif url.endswith('add') and arg1=='Shelley':
		body="""
{
  "items": [{
    "vault_type": "FUND_ESCROW",
    "description": "vault/add a PayPal",
    "json_to_be_encrypted": "{}"
  }]
}
""".encode('utf-8')
	elif url.endswith('mint'):
		body="""
{
"description": "Pay for Logo design",
"auto_operate": true,
"amount": 10000,
"return_transaction_data": true,
"inputs": [
{
"instrument_id": "b6e91c41-7b67-4759-8d67-5e9602f11060",
"account_type": "Card"
}
],
"outputs": [
{
"instrument_id": "56ffd03b-7bea-43e6-bf6a-2ed46b26dbd9",
"account_type": "PayPal"
}
]
}
""".encode('utf-8')

	print(body)
	#auth='Authorization: MODO0 key=uFiRj0L_RXG1b_BMlXeJA64dr1ySOexq'
	if method=='GET':
		r = requests.get(url, headers=headers)
	elif method=='POST':
		r = requests.post(url, headers=headers, data=body)

	R=''
	#r = requests.get('https://api.github.com/events')
	pp.pprint(r)
	print('r.text'+r.text)
	print('r.json:')
	print(r.json())
	print('r.content:'+str(r.content))

	if url.endswith('account_types'):
		for x in r.json():
			pp.pprint(x)
			pp.pprint(r.json()[x])
			for y in r.json()['response_data']:
				print(y) #list of account types
	elif url.endswith('register'):
		for x in r.json():	
			pp.pprint(x)
			pp.pprint(r.json()[x])
		print(r.json()['response_data']['user_id'])
	elif url.endswith('mint'):
		for x in r.json():	
			pp.pprint(x)
			pp.pprint(r.json()[x])
	elif url.endswith('vault/add'):
		for x in r.json():	
			pp.pprint(x)
			pp.pprint(r.json()[x])
#		print(r.json()['response_data']['vault_id'])
#		R=r.json()['response_data']['vault_id']
	return R

requester=None
submitter=None
		
def segmented_action(sender):
	# 0 = Me/Brandee view Default
	v['imageview'].hidden=True
	if sender.segments[sender.selected_index] == 'My Services':
		v.name='Shelley Graphic Artist'
		sender.segments=['BrandMe','Profile','Jobs']
		sender.selected_index = 1 #reset Brandee view to the 1st choice
		# Turn on Brander Profile
		tableviewBranderData.hidden = False #show the Brander data
		tableviewBranderProfileLabels.hidden = False #show the Brander data Labels
		tableviewBranderJobsAvail.hidden = True #hide the Jobs Available selector
		# Turn off other stuff
		tableviewBrandeeData.hidden = True #hide the Brandee data
		tableviewBrandeeProfileLabels.hidden = True #hide the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = True #hide the Services Available selector
	elif sender.segments[sender.selected_index] == 'Jobs':
		# Turn on Brander Available Jobs
		tableviewBranderData.hidden = True #hide the Brander data
		tableviewBranderProfileLabels.hidden = True #hide the Brander data Labels
		tableviewBranderJobsAvail.hidden = False #show the Jobs Available selector
	elif sender.segments[sender.selected_index] == 'Profile':
		# Turn on Brander Profile
		tableviewBranderData.hidden = False #show the Brander data
		tableviewBranderProfileLabels.hidden = False #show the Brander data Labels
		tableviewBranderJobsAvail.hidden = True #hide the Jobs Available selector
		submitter=MODO('add','Shelley')
	elif sender.segments[sender.selected_index] == 'Me':
		sender.segments=['BrandMe','My Profile','Services']
		sender.selected_index = 1 #reset Brandee view to the 1st choice
		v.name='Brand Dewayne'
		# Turn off Brander Profile
		tableviewBranderData.hidden = True #hide the Brander data
		tableviewBranderProfileLabels.hidden = True #hide the Brander data Labels
		tableviewBranderJobsAvail.hidden = True #hide the Jobs Available selector
		# Turn on Brandee
		tableviewBrandeeData.hidden = False #show the Brandee data
		tableviewBrandeeProfileLabels.hidden = False #show the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = True #hide the Services Available selector
	elif sender.segments[sender.selected_index] == 'Services':
		v['buttonSubmittedImage'].hidden=True
		tableviewBrandeeData.hidden = True #hide the Brandee data
		tableviewBrandeeProfileLabels.hidden = True #hide the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = False #hide the Services Available selector
	elif sender.segments[sender.selected_index] == 'My Profile':
		v['buttonSubmittedImage'].hidden=True
		tableviewBrandeeData.hidden = False #show the Brandee data
		tableviewBrandeeProfileLabels.hidden = False #show the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = True #hide the Services Available selector
		requester=MODO('add','Dewayne')
	elif sender.segments[sender.selected_index] == 'Review':
		tableviewBrandeeData.hidden = True #show the Brandee data
		tableviewBrandeeProfileLabels.hidden = True #show the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = True #hide the Services Available selector
		v['buttonSubmittedImage'].hidden=False
		v['imageviewFacebook'].hidden=False
		v['imageviewLinkedIn'].hidden=False
		v['imageviewTwitter'].hidden=False
		v['imageviewBrandMe'].hidden=False
	else:
		v.name='BrandMe'
		v['imageview'].hidden=False
		v['buttonSubmittedImage'].hidden=True
		sender.segments=['BrandMe','Me','My Services']
		sender.selected_index = 0 #reset Brandee view to the 1st choice
		# Turn on Brander Profile
		tableviewBranderData.hidden = True #show the Brander data
		tableviewBranderProfileLabels.hidden = True #show the Brander data Labels
		tableviewBranderJobsAvail.hidden = True #hide the Jobs Available selector
		# Turn off other stuff
		tableviewBrandeeData.hidden = True #hide the Brandee data
		tableviewBrandeeProfileLabels.hidden = True #hide the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = True #hide the Services Available selector		
		v['buttonSubmittedImage'].hidden=True
		v['imageviewFacebook'].hidden=True
		v['imageviewLinkedIn'].hidden=True
		v['imageviewTwitter'].hidden=True
		v['imageviewBrandMe'].hidden=True
		v['buttonSubmittedImage'].hidden=True
																
#def segmentedBrander_action(sender):
	# when the Brander takes an action
#	if sender.selected_index == 0: 
#		tableviewBranderProfileLabels.hidden = False
#		tableviewBranderData.hidden = False
#		tableviewBranderJobsAvail.hidden = True
#		tableviewBrandeeServiceAvail.hidden = True
#		tableviewBrandeeData.hidden = True
#		tableviewBrandeeProfileLabels.hidden = True
#	elif sender.selected_index == 1:
#		tableviewBranderProfileLabels.hidden = True
#		tableviewBranderData.hidden = True
#		tableviewBranderJobsAvail.hidden = False
#		tableviewBrandeeServiceAvail.hidden = True
#		tableviewBrandeeData.hidden = True
#		tableviewBrandeeProfileLabels.hidden = True
			
#def segmentedBrandee_action(sender):
#	if segmentedRole.selected_index == 0:
#		if sender.selected_index == 0:
#			tableviewBrandeeData.hidden = False
#			tableviewBrandeeProfileLabels.hidden = False
#			tableviewBrandeeServiceAvail.hidden = True
#			tableviewBranderJobsAvail.hidden = True
#			tableviewBranderProfileLabels.hidden = True
#			tableviewBranderData.hidden = True
#		elif sender.selected_index == 1:
#			tableviewBrandeeData.hidden = True
#			tableviewBrandeeProfileLabels.hidden = True
#			tableviewBrandeeServiceAvail.hidden = False
#			tableviewBranderJobsAvail.hidden = True
#			tableviewBranderProfileLabels.hidden = True
#			tableviewBranderData.hidden = True
#	elif segmentedRole.selected_index == 1:
#			segmentedBrander_action(sender)

def buttonSelectLogoJob_action(sender):
	v['buttonSubmit'].hidden = False
	v['labelSubmit'].hidden = False
	v['buttonSubmitImage'].hidden = False

def buttonSelectQuality_action(sender):
	v['buttonSubmit'].hidden = False
	v['labelSubmit'].hidden = False		

def buttonGetLogo_action(sender):
	v['tableviewBrandeeServiceAvail'].hidden = True
	v['tableviewQuality'].hidden = False

def buttonImageSubmitted_action(sender):
	v['tableviewBrandeeServiceAvail'].hidden = True
	v['imageSubmitted'].hidden = True

def buttonSubmitImage_action(sender):
	v['tableviewBranderJobsAvail'].hidden = True
	v['buttonSubmitImage'].hidden = True		
	tableviewBranderData.hidden = False
	tableviewBranderProfileLabels.hidden = False						

def buttonSubmittedImage_action(sender):
#	v['tableviewBranderJobsAvail'].hidden = True
	v['buttonSubmitImage'].hidden = True
	tableviewBranderData.hidden = False
	tableviewBranderProfileLabels.hidden = False						

def buttonSubmit_action(sender):
	if segmented.segments[segmented.selected_index] == 'Services':
		v['buttonSubmit'].hidden = True
		v['labelSubmit'].hidden = True
		v['tableviewQuality'].hidden = True
		segmented.selected_index = 1
		tableviewBrandeeProfileLabels.hidden = False
		tableviewBrandeeData.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBrandeeData.delegate.items=['Dewayne','MC end 8880','$100','$0']
		segmented.segments=['BrandMe','My Profile','Services','Review']
		segmented.selected_index = 1 #reset Brandee view to the 1st choice
	if segmented.segments[segmented.selected_index] == 'Jobs':
		v['buttonSubmit'].hidden = True
		v['labelSubmit'].hidden = True
		segmented.selected_index = 1
		v['buttonSubmitImage'].hidden = True
		tableviewBranderData.hidden = False
		tableviewBranderProfileLabels.hidden = False
		tableviewBranderJobsAvail.hidden = True
		tableviewBranderData.delegate.items=['Shelley','PayPal','$100','$0']
		MODO('mint',requester,submitter)
		
#v['imageview'].hidden=False
#	segmented.segments=['BrandMe','Me','My Services']
#	segmented.selected_index = 0 #reset Brandee view to the 1st choice

# load the coded UI to keep this in one file
v = ui.load_view_str(pyui.decode('utf-8'))
v['imageview'].image = ui.Image.named('brandme.jpg')
v['imageviewBrandMe'].image = ui.Image.named('brandme.jpg')
v['buttonSubmitImage'].image=ui.Image.named('dewwww.jpg')
v['buttonSubmittedImage'].image=ui.Image.named('dewwww.jpg')
v['imageviewFacebook'].image=ui.Image.named('facebook.jpg')
v['imageviewTwitter'].image=ui.Image.named('twitter.jpg')
v['imageviewLinkedIn'].image=ui.Image.named('linkedin.jpg')

# setup button responses
segmented = v['segmented'] # Determine if it is Me/Brandee or the Brander/Service Provider
segmented.action = segmented_action
#segmentedBrander = v['segmentedBrander'] # options for the Brander - Profile or Jobs Available
#segmentedBrander.action = segmentedBrander_action
#segmentedBrandee = v['segmentedBrandee'] # options for Me/Brandee - Profile or Services Available
#segmentedBrandee.action = segmentedBrandee_action

#put directly into the UI definition as actions on the buttons
#buttonSelectLogoJob = v['buttonSelectLogoJob'] # selectingLogoJob - Profile or Services Available
#buttonSelectLogoJob.action = buttonSelectLogoJob_action
#tableviewBranderJobsAvail = v['tableviewBranderJobsAvail'] #options when selecting a job
#tableviewBranderJobsAvail.action = tableviewBranderJobsAvail_action

# make it easier on the functions above
tableviewBrandeeServiceAvail=v['tableviewBrandeeServiceAvail']
tableviewBranderJobsAvail=v['tableviewBranderJobsAvail']
tableviewBrandeeData=v['tableviewBrandeeData']
tableviewBranderData=v['tableviewBranderData']
tableviewBrandeeProfileLabels=v['tableviewBrandeeProfileLabels']
tableviewBranderProfileLabels=v['tableviewBranderProfileLabels']

tableviewBrandeeData.delegate.items=['Dewayne','MC end 8880','$0','$0']
tableviewBranderData.delegate.items=['Shelley','PayPal','$0','$0']

v.present('sheet')
