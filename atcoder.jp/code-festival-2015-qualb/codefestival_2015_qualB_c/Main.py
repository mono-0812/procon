import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n,m=IIS()
ali=[False]*(10**5+100)
A=LIIS()
B=LIIS()
A.sort()
B.sort(reverse=True)
if m>n:
    print("NO")
    exit()
for i in range(m):
    if not B[i]<=A.pop():
        print("NO")
        exit()
print("YES")