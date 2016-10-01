def Decode(codes,s):
    ans=""
    while s:						#loop over a given encoding
        for k in codes:
            if s.startswith(k):		#check if any encoding occurs in dictionary
                ans+=codes[k]		#if any encoding is found, use it to form decoded 
                s=s[len(k):]		#move to remaining part of encoded string
    return ans

n=int(input("N:"))
codes={}
while n>0:
    s=input()
    #print(s[2:]+s[0])
    codes[s[2:]]=s[0]		#store charcters in dictionary with their encodings as keys 
    n-=1
st=input()
print(Decode(codes,st))
