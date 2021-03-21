import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
val=len(str(n))//2
tmp=0
if len(str(n))==1:
    print(0)
    exit()
for i in range(val-1):
    if tmp==0:
        tmp=9
    else:
        tmp=int(str(tmp)+"9")
val3=0
if int(str(n)[:val])<=int(str(n)[val:]):
    val3=int(str(n)[:val])
else:
    val3=int(str(n)[:val])-1
val2=0
if 10**(val-1)==0:
    val2=0
else:
    val2=10**(val-1)
val4=0
for i in str(n):
    val4+=int(i)
if val4==1 and len(str(n))%2==0:
    print(tmp)
elif len(str(n))%2==1:
    tmp=0
    for i in range(val):
        if tmp==0:
            tmp=9
        else:
            tmp=int(str(tmp)+"9")
    print(tmp)
else:
    print(val3+tmp-val2+1)
