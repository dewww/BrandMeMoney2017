import bz2
import ui
from base64 import b64decode

data = '''\
QlpoOTFBWSZTWSL0g5cAA7jfgFUQVOd/8D/nXY6/79/+UAPeHoJhYtmpBtUmpmhqanlP0Q
0mgAND1GmmgAAGgcwJiaDCZMmTIwmCaaZGJgCGA5gTE0GEyZMmRhME00yMTAEMAikhMNCn
iE1BtQGgBkGgHqGjQARJCI1T2qanhqT0TagMnqbKPUDJgCaeifqmmEe6pEVOtNXhPn3KtE
vHzJFbJE3JhKQbQCQSOMZZiqhmCj4UR82wpiMYDGBtBEtwuPlgmcHJSstvSfdOGl52xhaH
aMEpulJFIx+LQ4Eg7eH0fU5/C4UpysHLC9TbrInc22vRZK9V7HIm93kpREMNEQLEC1oUQj
e9JZL03lgtLN7pQBqvhTvDh6HnPVu32CgglkpKTpZ4ySOGCHkY5qlEOnqlbFNBqHZT+uWt
+uPQ9DWndV2hAgPW8hEKzb0F8SNB1eKQpTF2V+bFOPap9NsOTi1ocW8MjFXCwOjoMz7h1G
MrFMNjBjQGeTkZZk4sa2thyDKSRRzynqedwjRm3Fw645pw2RPPbJubiTGDNk4MGVeLVDKm
zisodFLRJmK5sbhrL8zqaopiwa0hE4VaQhZhZPXhwPQ7FWT0NIiszoiIDrKFYTvHGCulS3
mxl00eGm0qfCQfB9tE+riGc5u8SPAvkMmUb/MdnZJH1xoxsUrAemSJJ0ReRlaty6EqvzRt
uuFo+hbfTUlMJQGHuMIyM0JHskLt4DrCh6QveBNPA6hmpwh3KdszB6U5B05aDk1YjXapoD
LBZTMeYaTUwllJGgsDZKu6JWfyGt5wjxbkD5vwwFqNcV/NDNnyediFxoYGlOvaWP9YNmvB
hsnLyPj4guam2tL2kZDfeOGxHrUDlpmRGx4kjNM2FMcI8sS0pSEO4VRaC/qRT2i0iV5J5t
U2FtrqTAc4bzWlK5u+OowIx1Tdtb5DNgFJwNnG3EOUMn/kiQYHGMvgITyZhgZtcmE0e+MP
G82Y7EzfaVaDr/1AbQYcFwSxTodAaZqeKE7wcrZOk2/huL1RItgTim+k02AU8yu5TBN7uC
gXU2vGNLc1qVTTBSo7qRapsWtKHEPFAM03KTSvBAqYHv3SjFvOpITYnvCoSEQjSmV7/EbE
jA7Lh2J+3u87QE9rQV/4u5IpwoSBF6QcuA==
'''

pyui = bz2.decompress(b64decode(data))

def segmentRole_action(sender):
	if segmentRole.selected_index == 0:
		v['tableviewMeBranderData'].hidden = True
		v['tableviewMeBrandeeData'].hidden = False
	elif segmentRole.selected_index == 1:
		v['tableviewMeBranderData'].hidden = False
		v['tableviewMeBrandeeData'].hidden = True

v = ui.load_view_str(pyui.decode('utf-8'))

segmentRole = v['segmentedRole']
segmentRole.action = segmentRole_action

v.present('sheet')
