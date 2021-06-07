n,m=map(int,input().split())
import heapq
li=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append((a,b))
li.sort(reverse=True)
q=[0,1,1]
from heapq import heapify, heappop, heappush, heappushpop

class PriorityQueue:
    def __init__(self, heap):
        '''
        heap ... list
        '''
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)
q=PriorityQueue([])
t=0
ans=0
for i in range(m+1):
    for j in range(len(li))[::-1]:
        if li[j][0]==i:
            q.push(-li.pop()[1])
        else:
            break
    if len(q):
        ans+=-q.pop()

print(ans)