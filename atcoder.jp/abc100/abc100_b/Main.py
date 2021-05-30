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
d,n=IIS()
print(pow(100,d)*n if not ((pow(100,d)*n)%pow(100,d+1)==0) else pow(100,d)*n+pow(100,d))