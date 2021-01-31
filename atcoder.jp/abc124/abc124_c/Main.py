s=input()
flag=0
cnt=0
for i in s:
  if flag==2:
    flag =0
  if str(flag)!=i:
    cnt+=1
  flag+=1
print(min(cnt,len(s)-cnt))
  