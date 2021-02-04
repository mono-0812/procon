n=int(input())
h=list(map(int,input().split()))
lash=0
for i in h:
    if lash <= i:
        lash = i
        continue
    elif lash-1 <= i:
        lash = i+1
        continue
    else:
        print("No")
        exit()
print("Yes")

