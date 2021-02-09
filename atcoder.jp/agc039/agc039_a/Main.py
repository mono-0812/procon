sc=input()
k=int(input())
import copy
s=copy.deepcopy(sc)
las=""
cnt=0
cnt2=0
if len(set(list(s)))==1:
    print(len(s)*k//2)
    exit()
for i in range(len(s)):
    if las==s[i]:
        las=s[i]
        cnt+=1
        s = list(s)
        s[i]="."
        "".join(s)
    las=s[i]
s=copy.deepcopy(sc)+copy.deepcopy(sc)
las=""
for i in range(len(s)):
    if las==s[i]:
        las=s[i]
        cnt2+=1
        s = list(s)
        s[i]="."
        "".join(s)
    las=s[i]
print(cnt+(cnt2-cnt)*(k-1))