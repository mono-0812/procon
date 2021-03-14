n=int(input())
li=[]
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append(a)
    li.append(b)
    ab.append((a,b))
ans=float("inf")
for i in range(2*n):
    for j in range(2*n):
        s=li[i]
        g=li[j]
        val=0
        for k in range(n):
            val+=abs(s-ab[k][0])+abs(ab[k][0]-ab[k][1])+abs(ab[k][1]-g)
        ans=min(ans,val)
print(ans)