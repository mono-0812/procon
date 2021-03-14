n,m=map(int,input().split())
li=[set() for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    li[a].add(b)
    li[b].add(a)
for i in list(li[1]):
    if i in li[n]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")