import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n,c=IIS()
D=[LIIS() for i in range(c)]
C=[LIIS() for i in range(n)]
v=[[] for j in range(3)]
co=[[] for j in range(3)]
for i in range(n):
    for j in range(n):
        v[(i+j)%3].append(C[i][j]-1)
for ind in range(3):
    li=v[ind]
    for i in range(c):
        cost=0
        for j in range(len(li)):
            cost+=D[li[j]][i]
        co[ind].append((cost,i))
ans=INF
for co1,c1 in co[0]:
    for co2,c2 in co[1]:
        for co3,c3 in co[2]:
            if c1!=c2 and c2!=c3 and c1!=c3:
                ans=min(ans,co1+co2+co3)
print(ans)


