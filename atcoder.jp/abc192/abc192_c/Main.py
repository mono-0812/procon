n,k=map(int,input().split())
ans=str(n)
for i in range(k):
    g1="".join(sorted(ans,reverse=True))
    g2="".join(sorted(ans))
    ans=str(int(g1)-int(g2))
print(ans)