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
n=II()
li=[]
for i in range(n):
    x,y,h=IIS()
    li.append((x,y,h))
for cx in range(101):
    for cy in range(101):
        f=True
        st=[]
        for i in range(n):
            x,y,h=li[i]
            if h:
                H=h+abs(x-cx)+abs(y-cy)
                st.append(H)
        if len(set(st))==1:
            for x,y,h in li:
                if h!=max(st[0]-abs(x-cx)-abs(y-cy),0):
                    f=False
            if f:
                print(cx,cy,H)
                exit()