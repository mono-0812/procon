import collections
import itertools
import math
import decimal
import bisect
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n=II()
A=LIIS()
li=[A[0]]
for i in range(1,n):
    if A[i-1]!=A[i]:
        li.append(A[i])
if len(li)==1:
    print(1)
    exit()
st=1 if li[1]>li[0] else 0
ans=1
for i in range(1,len(li)):
    if li[i]>li[i-1]:
        if st==0:
            st=-1

        elif st==-1:
            st=1
            ans+=1
    else:
        if st==1:
            st=-1

        elif st==-1:
            st=0
            ans+=1
if st==-1:
    ans+=1
print(ans)