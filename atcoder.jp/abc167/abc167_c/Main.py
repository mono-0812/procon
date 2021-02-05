n,m,x=map(int,input().split())
b=[list(map(int,input().split())) for i in range(n)]
ans=1<<60
for i in range(1<<n):
    score=[0]*m
    money=0
    for j in range(n):
        if (1<<j) & i != 0:
            money+=b[j][0]
            for k in range(m):
                score[k]+=b[j][k+1]
    if min(score)>=x:
        ans=min(ans,money)
if ans==1<<60:
    print(-1)
else:
    print(ans)