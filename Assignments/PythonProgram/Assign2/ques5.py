s=list(input())
d=0
l=0
for i in s:
    if (ord(i)>=65 and ord(i)<=93) or (ord(i)>=97 and ord(i)<=123):
        l+=1
    if ord(i)>48 and ord(i)<58:
        d+=1
print("letter",l)
print("digits",d)