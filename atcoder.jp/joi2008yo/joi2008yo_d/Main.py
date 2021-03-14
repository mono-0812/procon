m=int(input())
mli=[]
for _ in range(m): mli.append(tuple(map(int,input().split())))
n=int(input())
nli=[]
for _ in range(n): nli.append(tuple(map(int,input().split())))
ns=set(nli)
for i in range(n):
    x0,y0=mli[0]
    movex=nli[i][0]-x0#引け
    movey=nli[i][1]-y0#引け
    flag=True
    for j in range(m):
        x,y=mli[j]
        if not (x+movex,y+movey) in ns:
            flag=False
            break
    if flag:
        ans=(movex,movey)
print(*ans)