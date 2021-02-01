n=int(input())
fl = True
li=[]
already=[]
for i in range(n):
    a = int(input())
    li.append(a)
t=li[0]
cnt=1
while fl:
    if t == 2:
        print(cnt)
        exit()
    t=li[t-1]

    cnt+=1
    if cnt==n:
        break
print(-1)


