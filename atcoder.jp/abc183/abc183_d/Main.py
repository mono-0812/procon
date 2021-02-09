n,w=map(int,input().split())
li=[]
time=0
total=0
for i in range(n):
    s,t,p=map(int,input().split())
    li.append((s,p))
    li.append((t,-1*p))
li.sort()
for t,p in li:
    if time!=t:
        
        if total>w:
            print("No")
            exit()
        time=t
    total+=p
print("Yes")