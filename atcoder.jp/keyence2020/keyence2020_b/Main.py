def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n=II()
li=[]
for i in range(n):
    x,l=IIS()
    li.append((x+l,x-l))
li.sort()
p=-float("inf")
ans=0
for i in range(n):
    if p<=li[i][1]:
        p=li[i][0]
        ans+=1
print(ans)