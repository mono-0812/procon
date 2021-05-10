import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
ragen=range
INF=10**10
MOD=10**9+7
##############################################################################
n=II()
A=LIIS()
odd=[]
even=[]
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
for i in A:
    #さんけたいかのやつどうするか
    while len(str(i))<3:
        i="0"+str(i)
    if int(str(i)[:-2])%2:
        odd.append(str(i)[-2:])
    else:
        even.append(str(i)[-2:])
odd.sort()
even.sort()
ans=0
cnt=0
for i in range(len(odd)-1):
    if odd[i]==odd[i+1]:
        if cnt==0:
            cnt=2
            continue
        cnt+=1
    else:
        if cnt>=2:
            ans+=combinations_count(cnt, 2)
        cnt=0
if cnt>=2:
    ans+=combinations_count(cnt, 2)
cnt=0
for i in range(len(even)-1):
    if even[i]==even[i+1]:
        if cnt==0:
            cnt=2
            continue
        cnt+=1
    else:
        if cnt>=2:
            ans+=combinations_count(cnt, 2)
        cnt=0
if cnt>=2:
    ans+=combinations_count(cnt, 2)
print(ans)