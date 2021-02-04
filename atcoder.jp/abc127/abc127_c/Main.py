n,m=map(int,input().split())
ml=0
mr=10**5
for i in range(m):
    l,r=map(int,input().split())
    ml=max(ml,l)
    mr=min(mr,r)
if ml>mr:
    print(0)
    exit()
print(mr-ml+1)
