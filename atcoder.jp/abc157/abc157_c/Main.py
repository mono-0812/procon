n,m=map(int,input().split())
nn=n
if m==0 and n==1:
  print(0)
  exit()
if m==0:
  print(10**(n-1))
  exit()
if n==1:
  n=9
if n==2:
  n=99
else:
  n=999
S=[]
C=[]
flag=0
cnt=0
for i in range(m):
  s,c=map(int,input().split())
  S.append(s)
  C.append(c)
for i in range(0,n+1):
  if len(str(i))<max(S):
    continue

  if len(str(i))!=nn:
    continue
  
  for n in S:
    if int(str(i)[n-1])==C[cnt]:
      flag+=1
    cnt+=1
  if flag==len(S):
    print(i)
    exit()
  flag=0
  cnt=0
print(-1)
