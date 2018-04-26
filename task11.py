from collections import OrderedDict
def dup_case():
	print(list(OrderedDict.fromkeys('abracadabra')))
dup_case()
