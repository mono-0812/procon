S = input()
cnt=0
ans=0
for i in S:
  if i in ["A","C","G","T"]:
    cnt+=1
  else:
    cnt=0
  ans = max(cnt,ans)
print(ans)