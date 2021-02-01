n=int(input())
li=list(map(int,input().split()))
mx=0
mxk=0
for i in range(2,max(li)+1):
    cnt=0
    for j in li:
        if j%i==0:
            cnt+=1
    if mx<cnt:
        mx=cnt
        mxk=i
print(mxk)
