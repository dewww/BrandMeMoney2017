import bz2
import ui
from base64 import b64decode

data = '''\
QlpoOTFBWSZTWQ68iKIAA7pfgFUQVOd/8D/nXY6/79/+UAPc9JTDW1NspBtUKaemmqn+pt
TaSPUCGEZGGgAAAAcwJiaDCZMmTIwmCaaZGJgCGA5gTE0GEyZMmRhME00yMTAEMAiUhNGj
ST9Cm0mnogNNPUaZGjQAD0jTQRJEQChpnqmQAGmjQ0DQDQ9QaaFiOdSIqelL3snblpVFrn
UkVqSJmSxKINUAkEjZZitFVC0FHYiPVjKMRjAYwNAIlui48sEzQcVKx0ejjPB0asJ+owqh
uGCUa0okUjHraDYJBu7MNjb+qwrTkYckXc6i4y3OTI4Y6ZlXh2JxPEUpJGNUQLEC1oUQje
9JZL03lktZvdKANi9pMhwe28B89eVgoIJZKSk4mcJJHBghtY2qlCHLtlMalw0hz0ejmz18
0eN42l28rkCBAfO7pEKzN6C+EjQebhkKUwuyuoxTc0Kb9sHFwtYh08gxMKuFgdLpGZtRxm
FYwpYqxiyOSyzJqeVRZWPHjCaU2iY7O2OMzkmXESxWIozgiwrZHLmaWFiaSIjiQxTfkKoN
HVQtg4uUJY85SGk8dKD5TbAvHOLmvFRIQs4tTw/uaKH6NCyThpQ4kNKD75K8siPM1LVXid
UV71WhbgTjdjI3ZeC+7DWznfHyj83Me0mrZtau2Y+mYrLenEPDDJFzEtEq2mJH+ctjfpWp
Qqdvb4uT1Fr8k0oCVBh5DCoqOUHloXLmHdCztDW8xqHxuI6lOaO+p3jcB2psG7TQNF7Eab
lLgZUFSlo6hol5YlSkjQWBslXdKVm5xrIelqQP87f6FqNmFctDMf8eBiFY0GBdRv3FR/WD
U04bGpNOh5N4KzE5LUzNY0HNmG/UjwVD3NGBJqd4ZgmDFMmgRL0vhLGXdQpmAL6tFZgL4E
sSUT9W3mGD7TM8AZGylK3uuOwYEY7E16G+IzOhSdBn3G4hpDE/5IkGBgMrsCE22hYMyOJh
LnvDHfejAdSYPvLNA6e2oO6DG9b0xqdToBryqeKE6wbrYOI0eHWXqiRbAnTmVDpzgU7yut
S9OJ1hULicjvjW3NqlmVL1LDxBMimobUqc4csByprUypbegWMHyXUmdzHWkTOm0KkkhAI0
pje/ONiRgclw5E9Xw+8KAn2aCv+LuSKcKEgHXkRRAA==
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
