import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
s=I()
cnt=0

q=queue.deque(list(s))
while len(q)>=2:
    a=q.popleft()
    b=q.pop()
    if a==b:
        continue
    elif a=="x":
        q.append(b)
        cnt+=1
        continue
    elif b=="x":
        q.appendleft(a)
        cnt+=1
        continue
    else:
        print(-1)
        exit()
print(cnt)

