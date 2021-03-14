n=int(input())
xy=[tuple(map(int,input().split())) for _ in range(n)]
xy_set=set(xy)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        x1,y1=xy[i]
        x2,y2=xy[j]
        if (x1+y1-y2,y1-x1+x2) in xy_set and (x2+y1-y2,y2-x1+x2) in xy_set:
            ans=max(ans,(x1-x2)**2+(y1-y2)**2)
print(ans)