import bisect,collections,copy,heapq,itertools,math,string,sys,queue
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
n,m=IIS()
path=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=IIS()
    path[a].append(b)
    path[b].append(a)
q=queue.Queue()
q.put(1)
ans=[0]*(n)
while not q.empty():
    np=q.get()
    ps=path[np]
    for i in ps:
        if not ans[i-1]:
            q.put(i)
            ans[i-1]=np
print("Yes")
for i in range(n-1):
    print(ans[i+1])