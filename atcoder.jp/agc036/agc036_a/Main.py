def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
s=II()
import math
print(0,0,10**9,1,10**9-(s%10**9) if 10**9-(s%10**9)!=10**9 else 0,math.ceil(s/10**9))