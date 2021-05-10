import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
ragen=range
INF=10**10
MOD=10**9+7
##############################################################################
n=II()
ans=0
while n>0:
    n-=100
    ans+=1
print(ans)