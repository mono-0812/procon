n,m=map(int,input().split())
wa=[0]*n
ac=[0]*n
penalty=0
for i in range(m):
    p,s=input().split()
    p=int(p)
    if s=="WA":
        wa[p-1]+=1
    elif ac[p-1]==0:
        penalty+=wa[p-1]
        ac[p-1]+=1
print(str(sum(ac))+" "+str(penalty))
    