n=int(input())
A=list(map(int,input().split()))
if len(set(A)) == len(A):
    print("YES")
    exit()
print("NO")
