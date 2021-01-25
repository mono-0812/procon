x,n=map(int,input().split())
pl=list(map(int,input().split()))
midif=0
cnt=0
ok=0
while ok==0:
  if x-cnt not in pl:
    print(x-cnt)
    exit()
  if x+cnt not in pl:
    print(x+cnt)
    exit()
  cnt+=1
  