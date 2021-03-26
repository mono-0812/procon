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
s=queue.deque(I());q=II()
flont=1
for i in range(q):
    query=list(input().split())
    if len(query)==1:
        flont*=-1
    else:
        if int(query[1])==1:
            if flont==1:
                s.appendleft(query[2])
            else:
                s.append(query[2])
        else:
            if flont==1:
                s.append(query[2])
            else:
                s.appendleft(query[2])
if flont==-1:
    s.reverse()
print("".join(s))