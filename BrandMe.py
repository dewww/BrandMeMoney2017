import bz2
import ui
from base64 import b64decode

data = '''\
QlpoOTFBWSZTWR8kLpkACLVfgFUQVOf/9T/3XY6/79/+YAce99ayyygPTpyrFCKKGDmmRk
MmCGjCYI00aMQNMmRgACCVUD0npPRBiANAAAAAAAADmmRkMmCGjCYI00aMQNMmRgACCJTS
R6kjIAeoaaAAGj1GmEaGh6QAEUmkKniehTaeiR6noQaA0aAGgADR6nqCKRMgJiamEymUHq
aaND1A0NAABoaLEcykCCvOje7Y3ZKJMVhToRhUJRiPNRyRshUAGMWSQAkBYQgSlK2oqqWo
AB3qAH2WkhhBhCAQgxDQgg8p/Pj7zP+71fAuv8pe90bbVgLGzQXeUab2zpu9np8/NWs83f
t28Dc4EUaELDLCGNCL0SI0OQ0RCkYowYhYbC5IkC58efgWxP+U5yGiMz584h9HiUfZ8Yvz
0igM+pZL1ZHcbHW4lsb79h512jBqPRtLF3cUEPdPc91Gw+EvVSQhGMGDeIhcgtVFskSCVW
tEZRrQasMgzEjJWBaAJYgcqPGhY6h5D6ZKaIaAwIyjRGgvOMGliGCZDAA9c24WgkGI4UCi
I6tVk1URdKdsMEGCjkMoPQP0GnloGBOw8riTx3Ert1xIO4MKhQspmXqNQgI/OFKHoHiQIT
wGs1DiMWjGwUSUF02fZ6JClMZhjbyBFL8VOs6FRikjQ3lNDQ7C7YkVqfMS6DlgXksrV8CY
0yJCG8d4xn2BuKXzH6iayHEINTCwDcQWcKWBccMcwhhtG4dSG4Iexj9DImH0kPM41GMjQv
zIuN9bs0uxuN5ia6rJMTWwmSgOgVjGxaDUztE2NxU7bK6xEDoQ5Q66bGYRQNtJGxaEzbMt
0zCRQqEFZloYmxlYEVCo3l5QsMDeamummQTLmdpcUCvaZWlNDuLszIUOMkGysuA20NkNMJ
iICRqMoEiyFyKlQIXcGBlDtIswtwnK8MgplRoG0GZPAeCCD8R9KPxerwLD9jiWHXehHPnl
0NTlQJ6y40oGfTY6GB0IJGA0wD3IaiSoWhkJmTu4uDTzMQ0ejYajSGFByBv9jSZuyGhj7F
NTAuaGAejlMzL+eYcuBUvM951uKByN7f0s4SwtM5VOu1OFhiEqTKmR86dMj5EM5P7DY/2n
gKXrmG2UM7xTLPc3MHC0ho3LDn2L1JonGQGtoC2YXKwy4uqzpNO7gxDx26EotasxvbyP3a
186P98vTRaCHMYHy/0NCYFR8ZofcA8ndjQj2Q6hCHKDpW44XnprP6E2znI+BMCGij/B+kh
Lzco+c5APpRxFy595bYvIC8YUf8zYcPBtUaxlAYOzfiW61RtqhIso75cjKpBEQJRZAZRoF
RzIzIW4xaHi1hfCF+TNmYgRNyHTJctTbbUg00GIGy7FqMhgGhA8PXaLQWFjKBJbwgmf6MB
YOwaC2DMloEo4YDyZRajaO7G34kcw2i0FnXz/AM48sDo4+wKXVEz4yhwxhwwwxAaxtRgNK
ukYUesaGuxL1qDDLnXR1Bw+KOhdXEo9tzo3no2I13KwuccMILg5QwZgd50JmPucMq+0a5S
4jhKaFhaBzdA7STI1zLCij2Vw9ooQDcLC1tJjMdhNqmeJ44TG7pkhIqISkQj6y58nfqNqq
R3ncDqcYwxG6yT8kQFUYBpBiglcpoYIUpXIsAQX9WBLyotSd6kkIGG4aeeJ0P+NBajzDj8
JWY+bohLtR9MB1UkM7kOV3hYvcA5SH18+G0IQJko+2hw7QHKuqj9d54hMfjlcvUcqAdcCg
aN84mBsoQUGkI1VTAi+3LVGcQJJKU4IBmo9xvRoF8cDyHmGznHMsBvEdw1oXD1F2nahvJD
ko3FsE52I1Vaj7IENKBgo+DuAJo76jf2L2kAOaNFGXVlmj+QYOeoraMShHn59eyzGe82Qu
PUjCO5HWhaJGQhAkRkgwhLKOG9foWkIMJIEhv3B30eD6PENhtB4bVK5Pm8jrMwZLdu/8Xc
kU4UJAfJC6ZA
'''

# ———————————————————— 

pyui = bz2.decompress(b64decode(data))

def segmentedRole_action(sender):
	# 0 = Me/Brandee view Default
	if sender.selected_index == 0:
		segmentedBrandee.selected_index = 0
		tableviewBranderData.hidden = True
		tableviewBranderProfileLabels.hidden = True
		tableviewBrandeeData.hidden = False
		tableviewBrandeeServiceAvail.hidden = False
# 1 = Brander view Default 
	elif sender.selected_index == 1:
		segmentedBrandee.selected_index = 0
		tableviewBranderData.hidden = False
		tableviewBrandeeData.hidden = True
		tableviewBranderProfileLabels.hidden = False
		tableviewBrandeeServiceAvail.hidden = True

def segmentedBrandee_action(sender):
	if segmentedBrandee.selected_index == 0:
		tableviewBrandeeData.hidden = False
		tableviewBrandeeProfileLabels.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
	elif segmentedBrandee.selected_index == 1:
		tableviewBrandeeData.hidden = True
		tableviewBrandeeProfileLabels.hidden = True
		tableviewBrandeeServiceAvail.hidden = False

def segmentedBrander_action(sender):
	if segmentedBrander.selected_index == 0:
		tableviewBranderProfileLabels.hidden = False
		tableviewBranderData.hidden = False
		tableviewBranderJobsAvail.hidden = True
	elif segmentedBrander.selected_index == 1:
		tableviewBranderProfileLabels.hidden = True
		tableviewBranderData.hidden = True
		tableviewBranderJobsAvail.hidden = False
	
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

