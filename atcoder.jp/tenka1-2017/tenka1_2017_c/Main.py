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
f=False
for i in range(1,3501):
    for j in range(1,3501):
        try:
            if (i*j*n)%(4*i*j-n*(i+j))==0 and 1<=(i*j*n)//(4*i*j-n*(i+j))<=3500:
                print(i,j,(i*j*n)//(4*i*j-n*(i+j)))
                f=True
                exit()
        except:
            if f:
                exit()
            pass