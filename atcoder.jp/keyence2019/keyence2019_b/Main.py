import copy
s=input()
o=0
fl=0
dif=0
las=""
key="keyence"
if s==key:
    print("YES")
    exit()
for i in range(len(s)):
    if s[:i]+s[i+1:]==key:
        print("YES")
        exit()
for i in range(0,len(s)-6):
    for j in range(6,len(s)+1):
        sc=s
        sc=sc[:i+1]+sc[j:]
        if sc==key:
            print("YES")
            exit()
print("NO")
