string=input()
p=0
for i in range(len(string)):
    if string[i]==".":
        p=i
print(string[p:])