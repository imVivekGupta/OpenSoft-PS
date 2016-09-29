def Decode(codes,s):
    ans=""
    while s:
        for k in codes:
            if s.startswith(k):
                ans+=codes[k]
                s=s[len(k):]
    return ans

n=int(input("N:"))
codes={}
while n>0:
    s=input()
    #print(s[2:]+s[0])
    codes[s[2:]]=s[0]
    n-=1
st=input()
print(Decode(codes,st))
