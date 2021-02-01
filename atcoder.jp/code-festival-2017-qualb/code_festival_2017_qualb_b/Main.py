from collections import Counter
n=int(input())
D=Counter(map(int,input().split()))
m=int(input())
T=Counter(map(int,input().split()))
for i in T:
    if not T[i] <= D[i]:
        print("NO")
        exit()
print("YES")
