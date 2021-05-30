import collections
import itertools
import math
import decimal
import bisect
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n=II()
R=[]
G=[]
B=[]
for i in range(n*2):
    a,c=input().split()
    if c=="R":
        R.append(int(a))
    elif c=="B":
        B.append(int(a))
    else:
        G.append(int(a))
if len(R)%2==0 and len(B)%2==0:
    print(0)
    exit()
def solve(a,b):
    res=10**18
    for i in range(len(a)):
        ind=bisect.bisect_left(b,a[i])
        try:
            res=min(res,abs(a[i]-b[ind]))
        except:
            pass
        try:
            if ind>0:
                res=min(res,abs(a[i]-b[ind-1]))
        except:
            pass
    return res
R.sort()
B.sort()
G.sort()
if len(R)%2==1 and len(B)%2==1:
    print(min(solve(R,B),solve(G,R)+solve(B,G)))
    exit()
elif len(G)%2==1 and len(B)%2==1:
    print(min(solve(G,B),solve(R,B)+solve(G,R)))
    exit()
elif len(G)%2==1 and len(R)%2==1:
    print(min(solve(G,R),solve(R,B)+solve(G,B)))
    exit()
