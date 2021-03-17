import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
S=I()
x=0;y=0;h=0
for i in S:
    if i=="L":
        x-=1
    elif i=="R":
        x+=1
    elif i=="U":
        y+=1
    elif i=="D":
        y-=1
    else:
        h+=1
T=II()
if T==1:
    print(abs(x)+abs(y)+h)
else:
    print(max(len(S)%2,abs(x)+abs(y)-h))