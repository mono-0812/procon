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
A=LIIS()
ans=0
A.sort(reverse=True)
SA=collections.Counter(A)
ans=0
for a in A:
    for i in range(1,32):
        val=1<<i
        if val-a*2:
            if SA[val-a]>0 and SA[a]>0:
                SA[val-a]-=1
                SA[a]-=1
                ans+=1
        else:
            if SA[val-a]>1:
                SA[val-a]-=2
                ans+=1


print(ans)