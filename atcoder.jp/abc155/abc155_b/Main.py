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
n=II()
A=LIIS()
for i in range(n):
    if not (A[i]%6==0 or A[i]%10==0 or A[i]%2==1):
        print("DENIED")
        exit()
print("APPROVED")