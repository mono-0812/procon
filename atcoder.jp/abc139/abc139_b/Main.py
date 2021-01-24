a,b=map(int,input().split())
total=1
cnt=0
while total<b:
  total+=a-1
  cnt+=1
print(cnt)