n=int(input())
x=list(map(int,input().split()))
ans=100000000
for i in range(min(x),max(x)+1):
    total=0
    for j in x:
        total+=(i-j)**2
    ans=min(total,ans)
print(ans)

