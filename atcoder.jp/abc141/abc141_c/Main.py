n,k,q=map(int,input().split())
point=[k]*n
minus=0
for i in range(q):
    minus+=1
    point[int(input())-1]+=1
mx = max(point)
for i in point:
    if i - minus> 0:
        print("Yes")
    else:
        print("No")