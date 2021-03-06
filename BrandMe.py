import bz2
import ui
from base64 import b64decode
import requests
import pprint
import time
import json

data = '''\
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
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
		v['imageviewFacebook'].hidden=True
		v['imageviewLinkedIn'].hidden=True
		v['imageviewTwitter'].hidden=True
		v['imageviewBrandMe'].hidden=True
	elif sender.segments[sender.selected_index] == 'Review':
		tableviewBrandeeData.hidden = True #show the Brandee data
		tableviewBrandeeProfileLabels.hidden = True #show the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = True #hide the Services Available selector
		v['buttonSubmittedImage'].hidden=False
		v['imageviewFacebook'].hidden=False
		v['imageviewLinkedIn'].hidden=False
		v['imageviewTwitter'].hidden=False
		v['imageviewBrandMe'].hidden=False
		tableviewBrandeeData.delegate.items=['Dewayne','MC end 8880','$0','$100']
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
