import collections
import itertools
import math
import decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
h,w=IIS()
C=[LIIS() for i in range(h)]
B=[[0]*w for i in range(h)]
W=[[0]*w for i in range(h)]
for i in range(h):
    v=0
    v2=0
    for j in range(w):
        if (i+j)%2==0:
            v+=C[i][j]
        else:
            v2+=C[i][j]
        B[i][j]=B[i-1][j]+v
        W[i][j]=W[i-1][j]+v2
ans=0
for i in range(h):
    for j in range(w):
        for i2 in range(i,h):
            for j2 in range(j,w):
                if i==i2 and j==j2:
                    if C[i][j]==0:
                        ans=max(1,ans)
                    continue
                else:
                    if i==0 and j==0:
                        if B[i2][j2]==W[i2][j2]:
                            ans=max(ans,(i2+1)*(j2+1))
                    elif i==0:
                        if B[i2][j2]-B[i2][j-1]==W[i2][j2]-W[i2][j-1]:
                            ans=max(ans,(i2+1)*(j2+1-j))
                    elif j==0:
                        if B[i2][j2]-B[i-1][j2]==W[i2][j2]-W[i-1][j2]:
                            ans=max(ans,(i2-i+1)*(j2+1))
                    else:
                        if B[i2][j2]-B[i-1][j2]+B[i-1][j-1]-B[i2][j-1]==W[i2][j2]-W[i-1][j2]+W[i-1][j-1]-W[i2][j-1]:
                            ans=max(ans,(i2-i+1)*(j2-j+1))

print(ans)