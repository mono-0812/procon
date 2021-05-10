import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
input = lambda: sys.stdin.readline().rstrip()
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
n,k=IIS()
k-=1
A=LIIS()
ans=INF
for i in range(n-k):
    if A[i]*A[i+k]<0:
        ans=min(ans,min(abs(A[i]),abs(A[i+k]))*2+max(abs(A[i]),abs(A[i+k])))
    else:
        ans=min(ans,max(abs(A[i+k]),abs(A[i])))
print(ans)
