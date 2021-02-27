s,t=input(),input()
ans=0
val=0
cnt=0
for i in range(len(s)-len(t)+1):
    cnt=0
    val=0
    for j in s[i:i+len(t)]:
        if j==t[cnt]:
            val+=1
        cnt+=1
    ans=max(val,ans)
print(len(t)-ans)