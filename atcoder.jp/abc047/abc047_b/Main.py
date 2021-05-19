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
def chmax(a: list, b: list) -> bool:
     assert len(a) == len(b) == 1, "1要素のlistを指定してください"
     if a[0] < b[0]:
         a[0] = b[0]
         return True
     return False
def chmin(a: list, b: list) -> bool:
    assert len(a) == len(b) == 1, "1要素のlistを指定してください"
    if a[0] > b[0]:
        a[0] = b[0]
        return True
    return False
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ragen=range
INF=10**10
MOD=10**9+7
##############################################################################
w,h,n=IIS()
xmx,xmi,ymx,ymi=w,0,h,0
for i in range(n):
    x,y,a=IIS()
    if a==1:
        xmi=max(x,xmi)
    if a==2:
        xmx=min(x,xmx)
    if a==3:
        ymi=max(y,ymi)
    if a==4:
        ymx=min(y,ymx)
if xmx-xmi>0 and ymx-ymi>0:
    print(max((ymx-ymi)*(xmx-xmi),0))
else:
    print(0)