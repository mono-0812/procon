n,a,b,c=input(),input(),input(),input()
ans=0
for i in range(len(a)):
    ans+=len(set([a[i],b[i],c[i]]))-1
print(ans)