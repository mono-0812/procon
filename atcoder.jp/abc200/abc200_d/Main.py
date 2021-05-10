import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
input = lambda: sys.stdin.readline().rstrip()
start_time=time.time()
from decimal import Decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
def nt(): print(time.time()-start_time);return
def comb(n, r):return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def try_run():
    try:tr()
    except:pass
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
ragen=range
INF=10**18
MOD=10**9+7
##############################################################################
n=II()
A=LIIS()[:12]
mod=[0]*200
def dfs(nm,li1,li2):
    if nm==len(A):
        if len(li1)<=0 or len(li2)<=0:
            return
        if li1==li2:
            return
        v1=0
        for i in li1:
            v1=(v1+i[0])%200
        v2=0
        for i in li2:
            v2=(v2+i[0])%200
        if v1==v2:
            print("Yes")
            print(len(li1),*sorted([i[1]+1 for i in li1]))
            print(len(li2),*sorted([i[1]+1 for i in li2]))
            exit()
        return
    li1.append([A[nm],nm])
    li2.append([A[nm],nm])
    dfs(nm+1,li1,li2)
    li1.pop()
    li2.pop()
    li1.append([A[nm],nm])
    dfs(nm+1,li1,li2)
    li1.pop()
    li2.append([A[nm],nm])
    dfs(nm+1,li1,li2)
    li2.pop()
    dfs(nm+1,li1,li2)
    return
dfs(0,[],[])
print("No")