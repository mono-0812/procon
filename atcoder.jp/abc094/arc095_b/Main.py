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

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def try_run():
    try:tr()
    except:pass
ragen=range
INF=10**10
MOD=10**9+7
##############################################################################
n=II()
A=LIIS()
A.sort()
m=A[-1]
print(m,min(A,key=lambda x:abs(m-x*2)))