from collections import deque
R,C=map(int,input().split())
s_0,s_1=map(int,input().split())
g_0,g_1 = map(int,input().split())
s_0,s_1,g_0,g_1=s_0-1,s_1-1,g_0-1,g_1-1
c=[list(input()) for i in range(R)]
queue = deque([[s_0,s_1]])
c[s_0][s_1]=0
while queue:
    x,y=queue.popleft()
    for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
        if c[x+i][y+j]==".":
            queue.append([x+i,y+j])
            c[x+i][y+j]=c[x][y]+1
print(c[g_0][g_1])