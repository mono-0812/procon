def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
a,b,k=IIS()
import sys
sys.setrecursionlimit(100000)
nCr = [[0]*(70) for i in range(70)]
for i in range(70):
    nCr[i][0]=1
nCr[1][1]=1
for i in range(65):
    for j in range(65):
        nCr[i][j]=nCr[i-1][j]+nCr[i-1][j-1]
ans=""
for i in range(a+b):
    if nCr[a+b-2][a-1]>=k:
        a-=1
        ans+="a"
    else:
        k-=nCr[a+b-2][a-1]
        b-=1
        ans+="b"
print(ans)

