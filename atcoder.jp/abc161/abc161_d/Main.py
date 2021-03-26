import bisect,collections,copy,heapq,itertools,math,string,sys,decimal,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def ZER(N): return [False for _ in range(N)]
INF=float("inf")
MOD=10**9+7
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
##############################################################################
k=II()
q=queue.Queue()
for i in range(1,10): q.put(i)
ans=[1,2,3,4,5,6,7,8,9]
for i in range(k):
    val=q.get()
    d=int(str(val)[-1])
    if d>0:
        ans.append(val*10+d-1)
        q.put(val*10+d-1)
    ans.append(val*10+d)
    q.put(val*10+d)
    if d<9:
        ans.append(val*10+d+1)
        q.put(val*10+d+1)
print(ans[k-1])

