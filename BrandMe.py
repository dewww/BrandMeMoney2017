import bz2
import ui
from base64 import b64decode

data = '''\
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
'''

# ———————————————————— 

pyui = bz2.decompress(b64decode(data))

def segmented_action(sender):
	# 0 = Me/Brandee view Default
	v['imageview'].hidden=True
	if sender.segments[sender.selected_index] == 'My Services':
		sender.segments=['Profile','Jobs']
		sender.selected_index = 0 #reset Brandee view to the 1st choice
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
	elif sender.segments[sender.selected_index] == 'Me':
		sender.segments=['My Profile','Services']
		sender.selected_index = 0 #reset Brandee view to the 1st choice
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
		tableviewBrandeeData.hidden = True #hide the Brandee data
		tableviewBrandeeProfileLabels.hidden = True #hide the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = False #hide the Services Available selector
	elif sender.segments[sender.selected_index] == 'My Profile':
		tableviewBrandeeData.hidden = False #show the Brandee data
		tableviewBrandeeProfileLabels.hidden = False #show the Brandee data labels
		tableviewBrandeeServiceAvail.hidden = True #hide the Services Available selector
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
		v['imageview'].hidden=False
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
	v['tableviewBranderJobsAvail'].hidden = True
	v['buttonSubmitImage'].hidden = True		
	tableviewBranderData.hidden = False
	tableviewBranderProfileLabels.hidden = False						

def buttonSubmit_action(sender):
	if segmented.segments[segmented.selected_index] == 'Services':
		v['buttonSubmit'].hidden = True
		v['labelSubmit'].hidden = True
		v['tableviewQuality'].hidden = True
		segmented.selected_index = 0
		tableviewBrandeeProfileLabels.hidden = False
		tableviewBrandeeData.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBrandeeData.delegate.items=['Dewayne','MC end 8880','$100','$0']
		segmented.segments=['My Profile','Services','Review']
		segmented.selected_index = 0 #reset Brandee view to the 1st choice
	if segmented.segments[segmented.selected_index] == 'Jobs':
		v['buttonSubmit'].hidden = True
		v['labelSubmit'].hidden = True
		segmented.selected_index = 0
		v['buttonSubmitImage'].hidden = False
		tableviewBranderData.hidden = True
		tableviewBranderProfileLabels.hidden = True
		tableviewBranderJobsAvail.hidden = True
		tableviewBranderData.delegate.items=['Shelley','PayPal','$100','$0']
		
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
