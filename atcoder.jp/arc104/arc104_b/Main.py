n,s=input().split()
n=int(n)
ans=0
for i in range(n):
    c1,c2=0,0
    S=s[i]
    if S=="A":
        c1+=1
    elif S=="T":
        c1-=1
    elif S=="C":
        c2+=1
    else:
        c2-=1
    for j in range(i+1,n):
        S=s[j]
        if S=="A":
            c1+=1
        elif S=="T":
            c1-=1
        elif S=="C":
            c2+=1
        else:
            c2-=1
        if c1==c2==0:
            ans+=1
print(ans)