for i in range(5):
    for j in range(5):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(4):
    for j in range(4):
        if i+j<4 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    