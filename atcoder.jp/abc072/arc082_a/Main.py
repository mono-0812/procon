n=int(input())
a=list(map(int,input().split()))
f = [0 for x in range(10**5+10)]
nmax=10**5
mx=0
for i in a:
    f[i]+=1
for i in range(nmax):
    mx=max(mx,f[i]+f[i+1]+f[i+2])
print(mx)