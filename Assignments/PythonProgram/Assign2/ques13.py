l=list(map(int,input().split(" ")))
x=[]
for i in l:
	if i not in x:
		x.append(i)
for i in x:
	print(i,end=" ")