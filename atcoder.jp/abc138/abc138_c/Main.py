n=int(input())
v=list(map(int,input().split()))
v.sort()
total=0
for i in range(n):
    if i == 0:
        total=v[i]
    else:
        total=(total+v[i])/2
print(total)

