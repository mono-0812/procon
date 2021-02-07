N,C=map(int,input().split())
event=[]
for i in range(N):
    a,b,c=map(int,input().split())
    a-=1
    event.append((a,c))
    event.append((b,-c))
event.sort()
ans=0
price=0
time=0
for x,y in event:
    if x!= time:
        ans += min(C,price) * (x-time)
        time=x
    price += y
print(ans)
