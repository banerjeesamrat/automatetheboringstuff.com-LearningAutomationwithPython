t
>>> birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
>>> birthdays['Shonu']='7 Sep'
>>> birthdays
{'Shonu': '7 Sep', 'Bob': 'Dec 12', 'Alice': 'Apr 1', 'Carol': 'Mar 4'}
>>> spam={'color':'red','age':42}
>>> for v in spam.values():
	print(v)

	
red
42
>>> for k in spam.keys():
	print(k)

	
color
age
>>> for i in spam.items():
	print(i)

	
('color', 'red')
('age', 42)
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
>>> spamlist=list(spam.keys())
>>> spamlist
['color', 'age']
>>> for k,v in spam.keys():
	print('Key: '+k+' Value: '+v)


>>> for k,v in spam.items():
	print('Key: '+k+' Value: '+str(v))

	
Key: color Value: red
Key: age Value: 42
