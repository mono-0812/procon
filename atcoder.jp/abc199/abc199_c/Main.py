import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
s=list(I())
q=II()
f=1
for i in range(q):
    t,a,b=IIS()
    if t==1:
        if f==1:
            val=s[a-1]
            s[a-1]=s[b-1]
            s[b-1]=val
        elif f==-1:
            if a+1<=n:
                a+=n
            else:
                a-=n
            if b+1<=n:
                b+=n
            else:
                b-=n
            val=s[a-1]
            s[a-1]=s[b-1]
            s[b-1]=val
    else:
        f*=-1
if f==-1:
    s=s[n:]+s[:n]
print("".join(s))