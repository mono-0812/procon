def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n=II()
A=LIIS()
aa=[]
sm=0
sm2=0
mx2=0
for i in range(1,n+1):
    sm+=A[i-1]
    mx2=max(mx2,A[i-1])
    print(mx2*i+sm+sm2)
    sm2+=sm

