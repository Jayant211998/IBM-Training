div=lambda l:[i  for i in l  if i%19==0 or i%13==0]
l=list(map(int,input().split(" ")))
print(div(l))