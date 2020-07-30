def fun(s):
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True
s=list(input())
print(fun(s))