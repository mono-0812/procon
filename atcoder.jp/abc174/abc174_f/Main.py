import bisect,collections,copy,heapq,itertools,math,string,sys,queue
from decimal import Decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def ZER(N): return [False for _ in range(N)]
INF=float("inf")
MOD=10**9+7
def make_divisors(n):
    odd=0
    even=0
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i%2==0:
                even+=1
            else:
                odd+=1
            if i != n // i:
                if (n//2)%2==0:
                    even+=1
                else:
                    odd+=1
        i += 1
    return (even,odd)

#　　　　　V
#　　 ／￣ψ￣＼
#　　| 合格祈願 |
#　　|＿＿＿＿＿|

##############################################################################
n,q=IIS()
bit=[0]*(n+4)
def add(a,i):
    while i<=n:
        bit[i]+=a
        i+=i&-i
def query(i):
    res=0
    while i>0:
        res+=bit[i]
        i-=i&-i
    return res
a=LIIS()
la=[-1]*n
li=[LIIS() + [_] for _ in range(q)]
li.sort(key=lambda x: x[1])
idx=0
ans=[0]*q
for l,r,xxx in li:
    l-=1
    for i in range(idx,r):
        if la[a[i]-1]==-1:
            add(1,i+1)
        else:
            add(-1,la[a[i]-1]+1)
            add(1,i+1)
        la[a[i]-1]=i
    idx=r
    ans[xxx]=query(r)-query(l)
for res in ans:
    print(res)