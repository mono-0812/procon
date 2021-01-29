n,m,t=map(int,input().split())
mx=n
lasb=0
for i in range(m):
  a,b=map(int,input().split())
  n-=((a-lasb)-0.5)//1+1
  if n<=0:
    print("No")
    exit()
  if mx !=n :
    n+=((b-a)-0.5)//1+1
  if mx <= n:
    n=mx
  lasb=b
n-=((t-lasb)-0.5)//1+1
if n<=0:
  print("No")
  exit()
print("Yes")