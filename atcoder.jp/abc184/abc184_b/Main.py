n,x = map(int,input().split())
s=input()
for i in s:
  if i == "o":
    x+=1
  if i == "x"and x != 0:
    x=x-1
print(x)