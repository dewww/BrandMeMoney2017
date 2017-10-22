import bz2
import ui
from base64 import b64decode

data = '''\
QlpoOTFBWSZTWeay7LMACLVfgFUQVOf/9T/3XY6/79/+YAce+i19zGgPTp1qVIiihmGSp6
nqAPUAaAAAGgAAAAAJVQPSek9EGIA0AAAAAAAAOaZGQyYIaMJgjTRoxA0yZGAAIJFNKZqI
AABoAAAGmQGhoABFEQppp6jUenkkaekBoaZGhoaYmgGjR6mgikTJommCmU8KaRppojRmpv
UyEAZNB6maSxHaUgQV40b3VHZllKRWFOZGFQojCOSNEZITgAYYWIiACIBYIICLLLbkVVLk
AA0qAHNcSMIMIQCEDCGRBB6jV085d/a0rrC/nrStaozsyBJfIuwozsaeu7kPYTynD5uLVt
trgRLJCw0YQ10IXchGY0GZCE0YUYGEJDIWiIgJZIaqB2iu5DTgFZBUMbEQ5Gws0W0eshIs
AqmBzL35HibnexLc2w3HpXeMWo9W8uXjzQQ+Y+X5kZC2ycQ2xjTTExTaEExiUQ0pIaGJVa
yjRGsjVhoDSKDQrAsgJYgb6OlCx0D4D65ZzwyDAjRGUZF4xgxYhgSgwAH1x4wSgSBhGygT
IR8vKSeUyLSnfDBBio5DKD2j7jT10DEncet4E+HElbjYkHiGNQoXUzMFGoQEfhClD2jzIE
J4jFUCo00oKWiBuAmjE6OJshIpUJqW8DSMOCnedCoxSRobFNDQ8C25IrU8iXYcsTAllevq
JjTIkIbDsMZ+AcSmEx+4msh4BBqY3AcSC7lS4LHLhmEMN42HUhsEPgx+JkTD7SHoc6jGRo
YZkWNq2zS3CxscDXVZJwNbiZKA7BWOFy0GpneJucSp1urrEQOhDlDrpuZhFA30kbl4TN8y
/TMJFCoQVmXhwNzK4IqFRwMChcYmxqa6aZBMszvLFAr1Mrymh4lszIUOMkGysuA20NkNMJ
iICRqMoEiyFyKlQIXcGBlDvIuxvxnLAMgplRoG8GZPEeSCD9J9qP0+/1Fx+RzLjvshHTpl
2NTzUCesudKB203OxidiCRiM4BzoaChULQylKUPLk28eJiGXm0mgxDCRyht8WkzjkNDh8V
NTEs0MQ5e2ZmYdMw83IqYGex3sUDzGzh2u5SxvM5VO+9OVxwCVJlTI+xO2R/BDOT+QpH9n
XCEtAopWGVq87Fcy3QuqEFm3IVdqcN2X3kAzzAlUWkhi4Xyk9Tr7LFoP2S2iZKU6nu9yPR
mt4Ef5jy2LYIaBgfJ+xsKAWj6aIdADi+yGYj5w5kEH+weq3DZdU/0fAI8TRH1pYQ2lHqPt
ImQvUeAxAeVHKLsaNJdVcQMgwo/5pYbm3qUaxsgMHhvyLdao21QoLRHcvRmqQRECSWYDNG
QXDojOYVxFk4d1b4G/LtbTECJ2IddC5amq2pBjIxA3W4NRkMA0IHl8LxaCwsZQJLYIJn6D
AUH0DIWgzmVAmjz5j6cxbhqP64vHBHQbRZFpu8fyDMO/A5+/3hS6ombXJNyMNyGGIDdG1G
AxVxGFHuGdrpS9agw0cy59YcOlHOujeUfG5kbzk0o17FYXMOGEFwb4YMwPQdiZw+XllX0m
uUuY4ymhcXgdHQOpJka5lxRR8K4+koQDYWFreTGY7ib1M+B9WMxt2yQkVEJSIR+BZ8/o1G
9VI9B4g6nOMeA2pQ6iICqMAzBkgouyZ2CFJrlWAIL+1AmBUWpPBSSEDDYafRE6H6mgtR6B
z/eVmPz9kJdUfvgO6khnZDzW9Vy+IDlIfh05bwhAmSj8iHLqA5V1Uf44H1BMfZKy9xyoB3
AkM/bN5gbJIJGYRqqmBF9uzVGmQElKU5IBmo+JsjQMI5HnPnG7pHQuBwEeI1oWHuLvO9DY
kOSjYvgnO5GqrUfjAhpQMVH1PEAmjtUcPBepADmjRRl3ZZo/4DFz1FbxiUI9Po18LuE9jd
Cx70YR4o4EEmhpsYwbQm2JjHJIVFOPoShAxMbYNlyYK4hdnmrwpCkxXZQ4v+SvrAVBYtWr
/xdyRThQkOay7LM=
'''

# ———————————————————— 

pyui = bz2.decompress(b64decode(data))

def segmentedRole_action(sender):
	# 0 = Me/Brandee view Default
	if sender.selected_index == 0:
		segmentedBrander.selected_index = 0
		tableviewBranderData.hidden = True
		tableviewBranderProfileLabels.hidden = True
		tableviewBrandeeProfileLabels.hidden = False
		tableviewBrandeeData.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBranderJobsAvail.hidden = True
# 1 = Brander view Default 
	elif sender.selected_index == 1:
		segmentedBrandee.selected_index = 0
		tableviewBranderData.hidden = False
		tableviewBrandeeData.hidden = True
		tableviewBranderProfileLabels.hidden = False
		tableviewBrandeeProfileLabels.hidden = True
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBranderJobsAvail.hidden = True

def segmentedBrander_action(sender):
	if sender.selected_index == 0:
		tableviewBranderProfileLabels.hidden = False
		tableviewBranderData.hidden = False
		tableviewBranderJobsAvail.hidden = True
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBrandeeData.hidden = True
		tableviewBrandeeProfileLabels.hidden = True
	elif sender.selected_index == 1:
		tableviewBranderProfileLabels.hidden = True
		tableviewBranderData.hidden = True
		tableviewBranderJobsAvail.hidden = False
		tableviewBrandeeServiceAvail.hidden = True
		tableviewBrandeeData.hidden = True
		tableviewBrandeeProfileLabels.hidden = True
	
def segmentedBrandee_action(sender):
	if segmentedRole.selected_index == 0:
		if sender.selected_index == 0:
			tableviewBrandeeData.hidden = False
			tableviewBrandeeProfileLabels.hidden = False
			tableviewBrandeeServiceAvail.hidden = True
			tableviewBranderJobsAvail.hidden = True
			tableviewBranderProfileLabels.hidden = True
			tableviewBranderData.hidden = True
		elif sender.selected_index == 1:
			tableviewBrandeeData.hidden = True
			tableviewBrandeeProfileLabels.hidden = True
			tableviewBrandeeServiceAvail.hidden = False
			tableviewBranderJobsAvail.hidden = True
			tableviewBranderProfileLabels.hidden = True
			tableviewBranderData.hidden = True
	elif segmentedRole.selected_index == 1:
			segmentedBrander_action(sender)

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
