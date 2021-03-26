h,w=map(int,input().split())
field=[list("".join(input())) for _ in range(h)]
import queue,copy
ans=0
for H in range(h):
    for W in range(w):
        q=queue.Queue()
        q.put((H,W))
        f=copy.deepcopy(field)
        if f[H][W]=="#":
            continue
        f[H][W]=0
        while not q.empty():
            x,y=q.get()
            if 0<=x+1<=h-1 and 0<=y<=w-1:
                if f[x+1][y]==".":
                    q.put((x+1,y))
                    f[x+1][y]=f[x][y]+1
            if 0<=x-1<=h-1 and 0<=y<=w-1:
                if f[x-1][y]==".":
                    q.put((x-1,y))
                    f[x-1][y]=f[x][y]+1
            if 0<=x<=h-1 and 0<=y+1<=w-1:
                if f[x][y+1]==".":
                    q.put((x,y+1))
                    f[x][y+1]=f[x][y]+1
            if 0<=x<=h-1 and 0<=y-1<=w-1:
                if f[x][y-1]==".":
                    q.put((x,y-1))
                    f[x][y-1]=f[x][y]+1
        ans=max(ans,f[x][y])
print(ans)
            
