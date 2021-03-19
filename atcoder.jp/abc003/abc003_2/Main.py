import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
ATC=["a","t","c","o","d","e","r"]
##############################################################################
s,t=I(),I()
for i in range(len(s)):
    if s[i]==t[i]:continue
    if (s[i]!="@" and t[i]!="@") or (s[i]=="@" and not t[i] in ATC) or (t[i]=="@" and not s[i] in ATC):
        print("You will lose")
        exit()
print("You can win")