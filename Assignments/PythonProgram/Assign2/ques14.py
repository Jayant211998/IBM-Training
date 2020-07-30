def fun(l):
	for i in range(len(l)):
			l[i]=l[i]*l[i]
	return l
l=[i for i in range(1,31)]
print(fun(l))