t=int(input("T?"))
ans=""
while t>0:
    s=input()
    for i in s:
        if i<='b':
            ans+=i
        elif i<='d':
            ans+='d'
        elif i<='h':
            ans+='h'
        else:
            ans+='p'
    print(ans)        
    t-=1
