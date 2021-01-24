n,a,b=map(int,input().split())
s=input()
total=0
rank=0
for i in range(n):
  if s[i]=="a":
    if total < a+b:
      total+=1
      print("Yes")
      continue
    else:
      print("No")
      continue
  if s[i]=="b":
    rank+=1
    if total < a+b and rank <= b:
      total+=1
      print("Yes")
      continue
    else:
      print("No")
      continue

  else:
    print("No")
    continue
