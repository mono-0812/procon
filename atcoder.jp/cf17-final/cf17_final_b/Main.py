import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=998244353
##############################################################################
s=collections.Counter(I())
li=[]
for i in s.keys():
    li.append(s[i])
li.sort()
if len(li)==3:
    if not (li[2]-1)*2<=li[1]+li[0]:
        print("NO")
    else:
        print("YES")
elif len(li)==2:
    if li[0]==li[1]==1:
        print("YES")
    else:
        print("NO")
else:
    if li[0]==1:
        print("YES")
    else:
        print("NO")


