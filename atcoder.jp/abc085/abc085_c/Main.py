n,y=map(int,input().split())
for i in range(0,n+1):
    for j in range(0,n+1):
        if i+j<=n:
            if i*10000+j*5000==y-(n-i-j)*1000:
                print(i,j,n-i-j)
                exit()
print(-1,-1,-1)