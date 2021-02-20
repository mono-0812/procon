W,H,x,y=map(int,input().split())
print(W*H/2,"01"[W==x*2 and H==y*2])