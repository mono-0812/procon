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
from decimal import Decimal as d
##############################################################################
n=II()
t=I()
li=[]
for i in range(n):
    li.append(t[i])
    if len(li)>=3:
        if li[-3]+li[-2]+li[-1]=="110":
            for i in range(3):li.pop()
if "".join(li) in {"01","011","0","101","1011","10","1","11",""}:
    if t=="1":
        print((10**10)*2)
        exit()
    if t[-1]=="0":
        print(10**10-t.count("0")+1)
    else:
        print(10**10-t.count("0"))
else:
    print(0)