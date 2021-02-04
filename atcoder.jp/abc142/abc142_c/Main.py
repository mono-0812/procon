n=int(input())
A=list(map(int,input().split()))
ans=[0]*n
cnt=1
for i in A:
    ans[i-1]=cnt
    cnt+=1
print(*ans)