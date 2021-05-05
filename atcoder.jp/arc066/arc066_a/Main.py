import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=10**10
MOD=10**9+7
##############################################################################
n=II()
A=LIIS()
li=[0 for i in range(-(-n//2))]
for i in A:
    if li[i//2]>1 or (i//2==0 and li[i//2]>0 and n%2):
        print(0)
        exit()
    li[i//2]+=1
ans=1
for i in li:
    ans=(ans*i)%MOD
print(ans)