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

n,m=IIS();A=LIIS()
li=[]
for i in range(m):
    b,c=IIS()
    li.append([c,b])
li.sort(reverse=True)
A.sort()
val=0
val2=0
tmp=0
while True:
    if li[val2][1]==0:
        val2+=1
    if len(li)-1<val2:
        break
    if len(A)-1<val:
         break
    if A[val]<li[val2][0]:
        tmp+=li[val2][0]-A[val]
        li[val2][1]-=1
        val+=1
    else:
        break
print(sum(A)+tmp)