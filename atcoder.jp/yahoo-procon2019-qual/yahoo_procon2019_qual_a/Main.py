n,k=map(int,input().split())
if n%2==1:
    n+=1
if n//2>=k:
    print("YES")
    exit()
print("NO")