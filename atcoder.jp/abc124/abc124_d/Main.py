import collections
import itertools
import math
import decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n,k=IIS()
s=I()
li=[[s[0],1]]
for i in range(1,n):
    if li[-1][0]==s[i]:
        li[-1][1]+=1
    else:
        li.append([s[i],1])
ans=0
ac=[0]+list(itertools.accumulate([li[i][1]for i in range(len(li))]))
if s[0]=="1":
    for i in range(1,len(li)+1):
        if i%2==0:
            ans=max(ans,ac[min(len(li),i+k*2-1)]-(ac[i-1]))
        else:
            ans=max(ans,ac[min(len(li),i+k*2)]-(ac[i-1]))
else:
    for i in range(1,len(li)+1):
        if i%2==1:
            ans=max(ans,ac[min(len(li),i+k*2-1)]-(ac[i-1]))
        else:
            ans=max(ans,ac[min(len(li),i+k*2)]-(ac[i-1]))
print(ans)