#a='{0:10b}'.format(6)
def hamming(s1,s2):
    assert len(s1)==len(s2)
    return sum(c1!=c2 for c1,c2 in zip(s1,s2))		#counts the no. of indices where bits of bin representation do not match

a = [int(x) for x in input().split()]		#taking space separated integers as input in a list
r = int(input("r?"))
m=11
for i in range(len(a)):					
    s=str('{0:10b}'.format(a[i]))			#converting no. to its binary representation
    hd=hamming(s,str(('{0:10b}'.format(r))))	#computing hamming distance b/w r and s 
    if hd<m:
        m=hd									#storing min hamming distance and its index
        ind=i
print(str(m)+" "+str(ind))
    #print(s)
