import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
N,H=IIS()
A,B,T=[],[],[]
for _ in range(N):
    a,b=IIS()
    A.append(a)
    B.append(b)
mxa=max(A)
for i in range(N):
    if B[i]>mxa:
        T.append(B[i])
T.sort(reverse=True)
if H<=sum(T):
    ans=0
    for i in range(len(T)):
        H-=T[i]
        ans+=1
        if H<=0:
            print(ans)
            exit()
else:
    print(math.ceil((H-sum(T))/mxa)+len(T))
    exit()


