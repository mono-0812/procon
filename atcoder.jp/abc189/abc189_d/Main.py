N=int(input())
ans=0
for i in range(1,N+1):
  s=input()
  if s=="OR":
    ans+=2**i
print(ans+1)