import itertools
import copy
n,m=map(int,input().split())
A=[]
B=[]
CD=[]
C=[]
D=[]
zero=[]
cnt=0
cntt=0
ans=0
for i in range(m):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)
k=int(input())
for i in range(k):
  c,d=map(int,input().split())
  CD.append([c,d])
  C.append(c)
  D.append(d)
  zero.append(0)
CC=[]
for i in range(2 ** k):
  CC=C.copy()
  for j in range(k):
    if ((i >> j) & 1):
      CC[j]=D[j]
  for j in range(m):
    if A[j] in CC and B[j] in CC:
      cnt+=1
  ans=max(cnt,ans)
  cnt=0
print(ans)