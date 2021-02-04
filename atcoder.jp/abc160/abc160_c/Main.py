k,n=map(int,input().split())
li=list(map(int,input().split()))
mxdif=0
for i in range(n):
    if i==n-1:
        mxdif=max(mxdif,k-abs(li[i]-li[0]))
    else:
        mxdif=max(mxdif,abs(li[i]-li[i+1]))
print(k-mxdif)