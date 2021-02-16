import sys
sys.setrecursionlimit(500000)
H,W=map(int,input().split())
L = [list(input()) for _ in range(H)]
def dfs(h,w):
    if not (0<=h<=H-1 and 0 <= w <= W-1) or L[h][w]=="#":
        return
    if L[h][w]=="g":
        print("Yes")
        exit()
    L[h][w]="#"
    dfs(h+1,w)
    dfs(h-1,w)
    dfs(h,w+1)
    dfs(h,w-1)

for i,j in enumerate(L):
    if "s" in j:
        dfs(i,j.index("s"))
        
        break
print("No")
