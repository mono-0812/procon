n=int(input())
li=[]
cnt=0
for i in range(n):
  x,y=map(int,input().split())
  li.append(str(x)+" "+str(y))
for i in li:
  x,y=map(int,i.split())
  if x==y:
    cnt+=1
  else:
    cnt=0
  if cnt==3:
    print("Yes")
    exit()
print("No")