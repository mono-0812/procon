import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
from typing import Deque
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
n,a=IIS()
s=I()
f=collections.deque()
b=collections.deque()
cnt,cnt2=0,0
for i in range(n)[::-1]:
    if s[i]=="#":
        if i<=a-1:
            f.append(i+1)
            cnt+=1
for i in range(n):
    if s[i]=="#":
        if i>a-1:
            b.append(i+1)
            cnt2+=1

for i in range((10**6)*2):
    f.append(0)
    b.append(n+1)
ans=0
mx1=0
mx2=0
for i in range(max(cnt,cnt2)):
    v=b.popleft()
    v2=f.popleft()
    ans+=(a-v2)*2
    ans+=(v-a)*2
    mx1=(a-v2)*2
    mx2=(v-a)*2
if cnt>=cnt2:
    ans-=(mx1//2)
else:
    ans-=mx1+(mx2//2)
print(ans)


