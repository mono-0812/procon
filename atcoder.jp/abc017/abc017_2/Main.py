import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
X=I()
ch=0
for x in X:
    if x in ["o","k","u"]:continue
    if x=="c":ch+=1;continue
    if (x=="h")*(ch==1):ch=0;continue
    print("NO");exit()
print("YES")