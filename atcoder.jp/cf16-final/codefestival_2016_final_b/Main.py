import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=10**10
MOD=10**9+7
##############################################################################
n=II()
val=0
ind=0
for i in range(n):
    val+=i+1
    if val>=n:
        ind=i
        break
ans=[]
for i in range(1,ind+2)[::-1]:
    if n-i>=0:
        n-=i
        ans.append(i)
    if val==0:
        break
ans.sort()
print(*ans)