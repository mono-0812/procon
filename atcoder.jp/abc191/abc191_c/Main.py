h,w=map(int,input().split())
field=[list("".join(input())) for _ in range(h)]
def ok(H,W):
    flag=0
    if field[H][W]=="#":
        flag+=1
    if field[H+1][W]=="#":
        flag+=1
    if field[H][W+1]=="#":
        flag+=1
    if field[H+1][W+1]=="#":
        flag+=1
    return int("01"[flag%2==1])
ans=0
for i in range(h-1):
    for j in range(w-1):
        if ok(i,j):
            ans+=1
print(ans)