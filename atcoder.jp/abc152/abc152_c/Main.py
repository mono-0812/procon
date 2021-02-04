n=int(input())
P=list(map(int,input().split()))
mi=0
cnt=0
for i in range(n):
    if i==0:
        cnt+=1
        mi=P[i]
        continue
    
    if P[i] <= mi:
        cnt+=1
    mi=min(mi,P[i])
print(cnt)