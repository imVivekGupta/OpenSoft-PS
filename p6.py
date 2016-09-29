T=int(input("T?"))
while T>0:
    N=int(input("N?"))
    a = [x for x in input().split()]
    flag=1
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j].startswith(a[i]) | a[i].startswith(a[j]):
                print("NO")
                flag=0
                break
        if flag==0:
            break
    if flag!=0:
        print("YES")
    T=T-1
