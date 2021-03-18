import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
P=LIIS()
S=""
for i in range(n):
    if P[i]==i+1:
        S+="o"
    else:
        S+=" "
li=S.split()
ans=0
for i in li:
    ans+=(len(i)+1)//2
print(ans)