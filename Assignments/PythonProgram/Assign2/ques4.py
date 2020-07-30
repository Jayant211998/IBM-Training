l=[-1 for i in range(51)]
def Fibonacci_series(Number):
    if(Number == 0):
        l[0]=1
        return 0
    elif(Number == 1):
        l[1]=1
        return 1
    else:
        if l[Number]!=-1:
            return l[Number]
        else:
            l[Number]=(Fibonacci_series(Number - 2) + Fibonacci_series(Number - 1))
            return l[Number]
for n in range(0, 51):
    print(Fibonacci_series(n), end = ' ')