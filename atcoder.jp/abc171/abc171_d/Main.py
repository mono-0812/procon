n=int(input())
a=list(map(int,input().split()))
q=int(input())
sa=sum(a)
li=[0]*(10**5+1)
for i in a:
    li[i]+=1
for _ in range(q):
    b,c=map(int,input().split())
    if li[b]>0:
        li[c]+=li[b]
        sa-=b*li[b]
        sa+=c*li[b]
        li[b]=0
    print(sa)


