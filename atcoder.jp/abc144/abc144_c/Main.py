n=int(input())
cnt=1
li=[]
while n>=cnt*cnt:
  if n%cnt==0:
    li.append(cnt+n/cnt)
  cnt+=1
print(int(min(li)-2))