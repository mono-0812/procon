import bisect,collections,copy,heapq,itertools,math,string,sys,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
q=collections.deque()
s=I()
state=1
for i in s:
    if i=="R":
        state*=-1
    else:
        if state==1:
            try:
                a=q.pop()
                if a==i:
                    continue
                q.append(a)
                q.append(i)
            except:
                q.append(i)
        else:
            try:
                a=q.popleft()
                if a==i:
                    continue
                q.appendleft(a)
                q.appendleft(i)
            except:
                q.appendleft(i)
if state==-1:
    ans="".join(q)[::-1]
else:
    ans="".join(q)
print(ans)

