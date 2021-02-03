n,m=map(int,input().split())
H=list(map(int,input().split()))
rmlist=[]
for i in range(m):
    a,b=map(int,input().split())
    if H[a-1]>H[b-1]:
        rmlist.append(b)
    elif H[a-1]<H[b-1]:
        rmlist.append(a)
    else:
        rmlist.append(a)
        rmlist.append(b)
print(n-len(set(rmlist)))