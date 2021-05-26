def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n=II()
ans=0
A,B=[],[]
for i in range(n):
    a,b=IIS()
    A.append(a)
    B.append(b)
ans=0
for i in range(n)[::-1]:
    ans+=(B[i]-((A[i]+ans)%B[i]) if ((A[i]+ans)%B[i])!=0 else 0)

print(ans)
