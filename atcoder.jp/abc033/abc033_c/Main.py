import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
s=list(input().split("+"))
ans=0
for i in s:
    try:
        if eval(i)!=0:
            ans+=1
    except:
        ans+=1
print(ans)