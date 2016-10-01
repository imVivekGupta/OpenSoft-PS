n=int(input("N:"))
L=[]
for i in range(1,n+1):
    U=list(range(1,i+1))		#form succesive elements of final list
    L.append(U)
print(L)
