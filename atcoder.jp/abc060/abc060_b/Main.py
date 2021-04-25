import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
st=set()
a,b,c=IIS()
n=a
while n%b not in st:
    st.add(n%b)
    n+=a
    if n%b==c:
        print("YES")
        exit()
print("NO")