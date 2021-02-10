n,m=map(int,input().split())
import heapq
A=list(map(int,input().split()))



ticket=0
if n<=1:
    A=list(A)
    for i in range(m):
        A[0]=A[0]//2
    print(A[0])
    exit()
A=list(map(lambda x: x*(-1),A))
heapq.heapify(A)
while ticket < m:
    val=(heapq.heappop(A)*-1)//2
    heapq.heappush(A,val*-1)
    ticket+=1
print(sum(A)*-1)