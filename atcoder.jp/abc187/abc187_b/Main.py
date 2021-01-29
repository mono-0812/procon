n=int(input())
xy=[]
for i in range(n):
  val=input()
  xy.append(val)
cnt=0
for i in xy:
  x,y=map(int,i.split())
  for m in xy:
    x2,y2=map(int,m.split())
    if x==x2 and y==y2:
      continue
    if (y-y2)/(x-x2) >= -1 and (y-y2)/(x-x2) <= 1:
      cnt+=1
print(cnt//2)
