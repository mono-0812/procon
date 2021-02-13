b,c=map(int,input().split())
ans=0
if c==1 and b==0:
    print(1)
    exit()
if c==1:
    print(2)
    exit()

if b<0:
    b*=-1
    ans=1
if b>0 and b*2<c:
    print(((b*2-1)*2)+(c-b*2)+1+ans)
elif b>0:
    print((c-1)*2+1+ans)
elif b==0:
    print(c+ans)
