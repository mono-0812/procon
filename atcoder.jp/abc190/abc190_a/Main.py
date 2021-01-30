#n=int(input())
a,b,c = map(int,input().split())
if a>b:
  if a-b>=1:
    print("Takahashi")
    exit()
if b>a:
  if b-a>=1:
    print("Aoki")
    exit()
if b==a:
  if c==0:
    print("Aoki")
    exit()
  else:
    print("Takahashi")
    exit()
  
