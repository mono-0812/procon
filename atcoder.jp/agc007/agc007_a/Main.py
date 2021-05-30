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
A=[I() for i in range(h)]
li=[]
for i in range(h):
    for j in range(w):
        if A[i][j]=="#":
            li.append((i,j))
li.sort()
for i in range(len(li)):
    if not sum(li[i])==i:
        print("Impossible")
        exit()
    if i>=1:
        if not li[i][0]-li[i-1][0]+li[i][1]-li[i-1][1]==1:
            print("Impossible")
            exit()
print("Possible")