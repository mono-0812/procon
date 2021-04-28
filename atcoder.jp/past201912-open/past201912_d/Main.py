import bisect,collections,copy,heapq,itertools,math,string,sys,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
li=[]
for i in range(n):
    li.append(II())
C=collections.Counter(li)
ans1=-1
ans2=-1
for i in range(1,n+1):
    if C[i]==2:
        ans1=i
    elif C[i]==0:
        ans2=i
if ans1==ans2==-1:
    print("Correct")
    exit()
print(ans1,ans2)




