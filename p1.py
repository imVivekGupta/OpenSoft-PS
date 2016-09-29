str1=input("A:")
str2=input("B:")
n=int(input("n:"))
i=0
while((i+n)<=len(str1)):
    s=str1[i:i+n]
    k=0
    while(k<len(str2)):
        j=str2.find(s,k,len(str2))
        if j!=-1:
            print(s+" "+str(i+1)+" "+str(j+1))
            k=j+1
        else:
            break                
    i+=1
