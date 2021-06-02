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
n,m=IIS()
li=[]
for i in range(m):
    x,y=IIS()
    li.append((x,y))
li.sort()
dic=collections.defaultdict(lambda:-1)
dic[n]=0
q=[]
las=0
for i in range(m):
    x,y=li[i]
    if las!=x:
        while len(q):
            i,j=q.pop()
            dic[i]=j
    las=x
    if 0<=dic[y+1]<=x-1:
        q.append((y,x))
        continue
    if 0<=dic[y-1]<=x-1:
        q.append((y,x))
        continue
    q.append((y,-1))
while len(q):
    i,j=q.pop()
    dic[i]=j
ans=0
for i in dic.keys():
    if dic[i]>=0:
        ans+=1

print(ans)