from collections import deque
n=int(input())
A=list(map(int,input().split()))
B=deque()
for i in range(n):
    if i%2==0:
        B.appendleft(A[i])
    else:
        B.append(A[i])
if n%2==0:
    B.reverse()
print(*B)