h=int(input())
ans=1
while h >= 2**ans:
    ans+=1
print(2**ans-1)