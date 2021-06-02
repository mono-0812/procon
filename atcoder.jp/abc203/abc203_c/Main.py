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
n,k=IIS()
pos=k
li=[]
for i in range(n):
    a,b=IIS()
    li.append((a,b))
li.sort()
for i in range(n):
    a,b=li[i]
    if pos>=a:
        pos+=b
print(pos)