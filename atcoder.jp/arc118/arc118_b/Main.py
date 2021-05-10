import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
input = lambda: sys.stdin.readline().rstrip()
from decimal import Decimal as d
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
start_time=time.time()
def nt(): print(time.time()-start_time);return
def comb(n, r):return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def try_run():
    try:tr()
    except:pass
ragen=range
INF=10**18
MOD=10**9+7
##############################################################################
k,n,m=IIS()
A=list(map(int,input().split()))
val=m/n
B=[0 for i in range(k)]
for i in range(k):
    B[i]=[math.floor(A[i]*val),i]
B.sort(key=lambda x:x[0]*n-A[x[1]]*m)
sb=0
for i in B:
    sb+=i[0]
val=m-sb
for i in range(k):
    if val<=0:break
    while val>0 and B[i][0]*n-A[B[i][1]]*m<0:
        B[i][0]+=1
        val-=1
    if i==k-1:
        B[i][-1]+=val
B.sort(key=lambda x:x[1])
print(*[x[0] for x in B])
def hyouka(li):
    mx=0
    for i in range(len(li)):
        mx=max(mx,abs(li[i]/m-A[i]/n))
    return