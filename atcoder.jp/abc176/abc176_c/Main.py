n=int(input())
A=list(map(int,input().split()))	
last=0
cnt=0
for a in A:
  if last>a:
    cnt+=(last-a)
  else:
    last=a
print(cnt)