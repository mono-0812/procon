h,w=map(int,input().split())
field=[]
for i in range(h):
    field.append(list(input()))
import queue
q=queue.Queue()
q.put((0,0))
field[0][0]=0
li=[(1,0),(0,1),(-1,0),(0,-1)]
while not q.empty():
    H,W=q.get()
    for i,j in li:
        if 0<=H+i<=h-1 and 0<=W+j<=w-1:
            if field[H+i][W+j]==".":
                q.put((H+i,W+j))
                field[H+i][W+j]=field[H][W]+1
cnt=0
for i in field:
    cnt+=i.count("#")
if field[h-1][w-1]=="." or field[h-1][w-1]=="#":
    print(-1)
    exit()
print(h*w-field[h-1][w-1]-cnt-1)
