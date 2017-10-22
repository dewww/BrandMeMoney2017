import bz2
import ui
from base64 import b64decode

data = '''\
QlpoOTFBWSZTWbzUgocABQtfgFUQVOf/8D/nXY6/79/+UAT972zba8HjuPQqiqwyp6Sept
E0yeo0amamJpgEYCeoMmjQMmDJNCniGRTCeoNAAAAAAAAJFNKmwpoAANGgABpo2oGgaDQC
KFFPST/U1T9EyhkekAAPUABhABp6gVJJoSmwhlPEp6TyJkGNTENNGg0MmnqNqXo5KQoAed
cXojdaagC6D4LCJSwudmMlkGCiVSSqqY45ZhImaEOqECykkDQDBiBg0VCBLF+WWscRQB9I
lhpZxkZM8gWVm3g9GG32VXRlMGiAhoh/iwLYuLSVJKKOUsMYlDTz7uuZ/BeLyeX1UtOnzY
YD4tdaOLW07NZoyazawtXKiOrwyeIukpMYwYQ0kQMUQwkmNEyckoSnILiChqKC65ZFOmh2
14lvdYdc5raaCRgZhJaS0nYU8yqUYlInoKjNB2emrLnSkqxSZ1FyFavXy3Xt5tN5q6pqIq
oSCsGDwtRf7jeomHeMrF6Z2pKWPV5apaRjiUt+BQkYokjPVweAjrLXXmeLAjQ5wEaJFXEK
BBADMCYKSoeMOwKWAIYlBBQJTZhU3WmoIIAPIeUPjGJ5kFziEyTh0Ng2lRErzJrMQCmgFj
AKZGQsQiKCyu8obaNMDVWFKMaXzUwcaAQaopmVQLHBhV0nznc3beBYKnwvLsdVujEtwvwt
uYsoPZI4wFCm5K1YRVBAJ2E29OThLCS9HWMESi/SkqvJRMRnJbQdKy1SPV6kGNyepKWoBS
McKMAfRboUs6X1S9laYyNWynFYeoGSOxiYuDtaqV1hRFwbAGeBMKHgAg2hwV5hMVdHKInc
WrIosISp2pBaqnDYFtOYiqQOYHTJXL+nRT9yzHFrYZX9frk9uXbJ9Pt2xcm8o8f9loyPPm
foG96amCHzb/eOMXNEcp/XyVsk8ZnDZJPf99k0apJ9beHsk8Q1cerO8cO8Uhbju7Q1hTFL
1bLvASugvWhYgZSgClluDFarPSLef5dMmrZq2Cdx8b5xf/bssbW34CsdGmZlihejdkLio0
2Tmlu0qf8UMC3z4mEm/eeHYLzI7uSa+9JymQsMPR+pyndRt6/AHXeTmrjXRwVVV4DGSnCT
gVJNrDqNMdIwZJgHU5l0p1uyr3XQufYtblITENV53jgKHsbKw9fZyY6+jcUW644ONNlsJJ
tv4b0OcVFFGldN1tvBIYcO+s51JXcZjZiF6DHEBgF36SZKRjS0cWmktfOKK0a6kxFaTJKK
ZnJa/ULm5zefHA8m+TdJ3z2GOiTho67x0BqsfLftHOmqSdUbuAY80k/LR2MCso4nJdPRLD
yGgumJCYQpR1xbVSzmBkNeoExVyXMaK8h3+mMkOQvkyOgZJgaJJfK2uTlkmQcYwdJWyG8u
NwYZJtgAxW9WbLzm+2xJGJVqG3y7Oe/RhtM3bJUmqT4JapSlEokkqCc8YEJNLBMWBKz1O9
SDE/RgyUKEQf4u5IpwoSF5qQUO
'''

# ———————————————————— 

pyui = bz2.decompress(b64decode(data))

def segmentRole_action(sender):
	if sender.selected_index == 0:
		v['tableviewMeBrandeeData'].hidden = False
		v['tableviewMeBranderData'].hidden = True
		v['tableviewMeProfileLabels'].hidden = False
		v['tableviewBrandeeServiceAvail'].hidden = True
	elif segmentRole.selected_index == 1:
		v['tableviewMeBranderData'].hidden = False
		v['tableviewMeBrandeeData'].hidden = True
		v['tableviewMeProfileLabels'].hidden = True
		v['tableviewBrandeeServiceAvail'].hidden = True

def segmentBrandee_action(sender):
	if segmentBrandee.selected_index == 0:
		v['tableviewMeProfileLabels'].hidden = False
		v['tableviewMeBrandeeData'].hidden = False
		v['tableviewBrandeeServiceAvail'].hidden = True
	elif segmentBrandee.selected_index == 1:
		v['tableviewMeProfileLabels'].hidden = True
		v['tableviewMeBrandeeData'].hidden = True
		v['tableviewBrandeeServiceAvail'].hidden = False
					
v = ui.load_view_str(pyui.decode('utf-8'))

segmentRole = v['segmentedRole']
segmentRole.action = segmentRole_action
segmentBrandee = v['segmentedBrandee']
segmentBrandee.action = segmentBrandee_action

v.present('sheet')

