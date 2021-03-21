import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
li=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ans=INF
n=II()
X=LIIS()
def bit(nm,sm):
    if nm==len(li):
        for i in X:
            if math.gcd(sm,i)==1:
                return
        global ans
        ans=min(sm,ans)
        return
    bit(nm+1,sm*li[nm])
    bit(nm+1,sm)
    return
bit(0,1)
print(ans)


