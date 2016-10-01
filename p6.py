T=int(input("T?"))
while T>0:
    N=int(input("N?"))
    a = [x for x in input().split()]
    flag=1
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j].startswith(a[i]) | a[i].startswith(a[j]):		#given encoding is not good if any charcater does 
                print("NO")		#if not good, encoding of char not present at leaf must be the initial part of encoding of char at leaf
                flag=0
                break
        if flag==0:
            break
    if flag!=0:
        print("YES")
    T=T-1
