import bz2
import ui
from base64 import b64decode

data = '''\
QlpoOTFBWSZTWREr4wIACLVfgFUQVOf/9T/3XY6/79/+YAb+A+j7KAGmbJQRRQhzTIyGTB
DRhMEaaNGIGmTIwABDmmRkMmCGjCYI00aMQNMmRgACHNMjIZMENGEwRpo0YgaZMjAAEEim
oNJAANBkAAB6gAAAACJTRJNDINMSjT9Ig9QHlPUZG1PSZHqGhk9NQRUJk0ExNAESD0EaYg
aaaAGmI0MmEeJSCCvYjofCePBZKl4p3IxUKRiPCjhGyFQAYxZJACQFhCBMYyzIqqZkAA3K
AHdmLDEGIQEIMQzoIP9nh7PUZv+vV94X2+5L3uLbTZbGiwvCo24d3uzdv5Hn6r3rq+vw5n
J1ks2IsaYhvoReUiNDgaIhSMUYMQsNhcIkF069vzGaV/ibbDhGjz6JH0dZh8vXM+nimAa+
Mvb3YnaanWpHU23ajxprC9oPNtLF2cEEPCd/woxHpL1UkIRjBg3iIXILVRbJEgl1vZGkb2
G7GkaoaLwWwCYQOlHoQw7R8x38FtUbAwRpGyNhewYbGRgikTADiegyTEMTQppAQNCttki2
B1jK2DAgXqOIxgecfuM/BMLyVh4HAlhsI12VIh2hfQJlk8i5RoEAh/EFJnnHgQEJXjKkCm
00oJ3CBuAoRhce82QkTqE1LaBpFmAp1lMoMJxMzaTzMzcV1IlKH2Eeg43lxHG1e4kM8SIh
tHaMMtwbCd0h+8ksRwCBoX2AbCBZvnYFTfhkEGDaNR0INQg7mHqMSQegg8jhQYYmZdkQqb
aVySuFTaYGmixTA0sJEYB0CkMLFmNDK0TU2FDnZTSEIDmQcYOmepkEJhrnE1LQka5FueQR
JlAgUkWhgamNgQoFBuLiZYXm00NM88QkVZWlSYU5mNpPM7SuRiYG/YW/PS4DdqbjKt+OYV
NduAVKTuNK4BO7eYmybrEsvtvlG4MQnjNmGsDIleO9BB8p6EfL7u4sPWcCw67UIcuWPQ0O
MwlpHhOYZdNToXnQgRLxjwD1IbSi4ZBwFVR9Ofm2dTI2e7cbTYGuw8AcnRnI2YjMw+Kehe
VZl4cPPIyLuWQcd5QuMtp1qTDibW7pZvjfaZRoddZ77DAIzkUMT7U6Yn1IZRfWMT+zOchL
NJqVLK11OmugvzOlQgsvyFXcohux9owUYYEqhKmQnQJWyV0u8EybNmWM4JSio5OVC7OPL7
Effs7cLgQ2jB+j/RwUBkPXSH6gOx++MhHsDgQIHtB5rYNV0T2HvCHaZi+BKiGaj7T1REuN
ij4ziA+lHAXHl3i2xeIFwxR+DWDn5vBRvNIDD5dGdc2SjldChaR5TMjSpCSCWWgGkbBceJ
GqDLfFieTsFxvzzYQET4Ie6RtWw/6lhA4xGEBsrg0GwwHBB5vhmFwLFnDBLcgQo8BgYHcN
hcDVGQFI69Y+bSLcch8d90Z0eIchbC15Oz1hxj0wdXl+QUzXE498sc8188YyB5ByFgbFdg
xR+I1N9yaFuDGnjXVvDr9iOpdvQo/O8aOg9G5G/irF4x164Zg6Q1tAbjoSMO/vxp8hpjHg
N8ZIWFoHJzDmRYmmRYTUd1L/kJkAaiwWlpIZDqJrQywPNfIa9MUIlFCMSCPvKvZ3tBtVSH
eO0HQ4QvwGs5HtIQLowG0M8KXSamEUtfgWAQ0ckEzmQtCVykUIDBqM/HCUz4GYtB5Bw8hS
Q+LohHmj6YB1UiMqoca91i9oDjEffy36wQgJio/Khv5gONNFH8LjzBIfpjVeo4zXqBENXK
dDBxYhYbRG6qayaMtNxazglkxjmQDJR7TajMLobzsPENnKHIsBuEdg0mVHqLrK1DaRHFRq
WwJSsRoq0H41gzmF6j3OxWSO2g3bl5kAHJGajHqxyR/cL3LQVtGEYI8vHpuswltNUKnuRg
jsR9iEYJGQhAkRkgwhLKO83r3i0hBhJAkPTcH0o9v8PcNhtB/S1Su/93vfaZBhbt3/xdyR
ThQkBEr4wIA=
'''

# ———————————————————— 

pyui = bz2.decompress(b64decode(data))

def segmentedRole_action(sender):
	# 0 = Me/Brandee view Default
	if sender.selected_index == 0:
		segmentedBrander.selected_index = 0
		tableviewBranderData.hidden = True
		tableviewBranderProfileLabels.hidden = True
		tableviewBrandeeData.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBranderJobsAvail.hidden = True
# 1 = Brander view Default 
	elif sender.selected_index == 1:
		segmentedBrandee.selected_index = 0
		tableviewBranderData.hidden = False
		tableviewBrandeeData.hidden = True
		tableviewBranderProfileLabels.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBranderJobsAvail.hidden = True

def segmentedBrandee_action(sender):
	if segmentedBrandee.selected_index == 0:
		tableviewBrandeeData.hidden = False
		tableviewBrandeeProfileLabels.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBranderJobsAvail.hidden = True
	elif segmentedBrandee.selected_index == 1:
		tableviewBrandeeData.hidden = True
		tableviewBrandeeProfileLabels.hidden = True
		tableviewBrandeeServiceAvail.hidden = False
		tableviewBranderJobsAvail.hidden = True

def segmentedBrander_action(sender):
	if segmentedBrander.selected_index == 0:
		tableviewBranderProfileLabels.hidden = False
		tableviewBranderData.hidden = False
		tableviewBranderJobsAvail.hidden = True
		tableviewBrandeeServiceAvail.hidden = True
	elif segmentedBrander.selected_index == 1:
		tableviewBranderProfileLabels.hidden = True
		tableviewBranderData.hidden = True
		tableviewBranderJobsAvail.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
	
v = ui.load_view_str(pyui.decode('utf-8'))

segmentedBrandee = v['segmentedBrandee']
segmentedBrandee.action = segmentedBrandee_action
tableviewBrandeeData=v['tableviewBrandeeData']
tableviewBranderData=v['tableviewBranderData']
tableviewBrandeeProfileLabels=v['tableviewBrandeeProfileLabels']
tableviewBranderProfileLabels=v['tableviewBranderProfileLabels']
segmentedRole = v['segmentedRole']
segmentedRole.action = segmentedRole_action
segmentedBrander = v['segmentedBrander']
segmentedBrander.action = segmentedBrander_action
tableviewBrandeeServiceAvail=v['tableviewBrandeeServiceAvail']
tableviewBranderJobsAvail=v['tableviewBranderJobsAvail']

v.present('sheet')
