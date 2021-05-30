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
print("YNeos"[not n==m::2])