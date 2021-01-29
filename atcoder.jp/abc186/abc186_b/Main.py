h,w=map(int,input().split())
li=[]
cnt=0
for i in range(h):
  l=list(map(int,input().split()))
  for b in l:
    li.append(b)
val=min(li)
for i in li:
  cnt+=i-val
print(cnt)
  	

