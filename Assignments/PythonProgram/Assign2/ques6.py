password=list(input())
pt=0
if len(password)>=6 and len(password)<=16:
	pt+=1
l=[i for i in range(48,57)]
for i in l:
	if chr(i) in password:
		pt+=1
		break
l=[i for i in range(65,93)]
for i in l:
	if chr(i) in password:
		pt+=1
		break
l=[i for i in range(97,123)]
for i in l:
	if chr(i) in password:
		pt+=1
		break
if '$' in password or '#' in password or '@' in password :
	pt+=1
if pt==5:
	print("Valid")
else:
	print("Invalid")
