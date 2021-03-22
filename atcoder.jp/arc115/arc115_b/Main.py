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
C=[LIIS() for _ in range(n)]
li2=[]
for i in range(n):
    li=[]
    for j in range(n):
        li.append(C[0][j]-C[i][j])
    if not len(set(li))==1:
        print("No")
        exit()
    li2.append(li[i])
print("Yes")
val=C[li2.index(max(li2))]
li3=[]
for i in li2:
    li3.append(abs(i-max(li2)))
print(*li3)
print(*val)