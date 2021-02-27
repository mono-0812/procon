n=int(input())
li=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append((b,a))
li.sort()
time=0
for b,a in li:
    time+=a
    if time>b:
        print("No")
        exit()
print("Yes")

    
