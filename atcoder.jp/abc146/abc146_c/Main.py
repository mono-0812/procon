a,b,x=map(int,input().split())
ans=0
for i in range(1,100000):
    if i<len(str((x-b*i)//a)):
        continue
    ans=(x-b*i)//a
    break
if ans<0:
    print(0)
    exit()
if int(ans)>10**9:
    print(10**9)
    exit()
print(int(ans))