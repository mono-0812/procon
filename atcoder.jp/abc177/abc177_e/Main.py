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
sa=set(A)
P=True
if len(sa)==1:
  if A[0]==1:
    print("pairwise coprime")
  else:
    print("not coprime")
  exit()
for i in range(2,10**6+1000):
    cnt=0
    for j in range(i,10**6+1000,i):
        if j in sa:cnt+=1
    if cnt>=2:
        P=False
ans=math.gcd(A[0],A[1])
for a in A:
    ans=math.gcd(ans,a)
if P:
    print("pairwise coprime")
elif ans==1:
    print("setwise coprime")
else:
    print("not coprime")