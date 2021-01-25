s=input()
cnt=0
w=0
for i in s:
  if i == "W":
    cnt+=w
  if i == "B":
    w+=1
print(cnt)