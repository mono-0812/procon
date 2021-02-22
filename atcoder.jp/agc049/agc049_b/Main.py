n=int(input())
s=input()
t=input()
res1,res2,cnt=0,0,0
for i in range(n):
    if t[i]=="1":
        res2+=i
        cnt+=1
    if s[i]=="1":
        if cnt>0:
            res1+=i
            cnt-=1
        else:
            res2+=i
            cnt+=1

if cnt>0:
    print(-1)
else:
    print(res1-res2)
