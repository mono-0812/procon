n,x=map(int,input().split())
total=0
for i in range(1,n+1):
  v,p=map(int,input().split())
  total+=v*p
  if total > x*100:
    print(i)
    exit()
print(-1)