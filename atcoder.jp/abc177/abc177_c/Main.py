n=int(input())
Alis=list(map(int,input().split()))
lis=Alis
sm=0
mod = 10**9 + 7
total=0
for b in Alis:
  total += sm*b
  sm+=b
  
  
print(total%mod)
  