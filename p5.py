#a='{0:10b}'.format(6)
def hamming(s1,s2):
    assert len(s1)==len(s2)
    return sum(c1!=c2 for c1,c2 in zip(s1,s2))

a = [int(x) for x in input().split()]
r = int(input("r?"))
m=11
for i in range(len(a)):
    s=str('{0:10b}'.format(a[i]))
    hd=hamming(s,str(('{0:10b}'.format(r))))
    if hd<m:
        m=hd
        ind=i
print(str(m)+" "+str(ind))
    #print(s)
