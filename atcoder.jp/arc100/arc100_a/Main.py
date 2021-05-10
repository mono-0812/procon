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
n=II()
A=LIIS()
B=[A[i]-i-1 for i in range(n)]
B.sort()
if n==0:
    print(0)
    exit()
val=B[(n-1)//2]
ans=INF
cnt=0
for i in range(n):
    cnt+=abs(A[i]-i-1-val)
ans=min(ans,cnt)
val=B[(n)//2]
cnt=0
for i in range(n):
    cnt+=abs(A[i]-i-1-val)
ans=min(ans,cnt)
print(ans)
