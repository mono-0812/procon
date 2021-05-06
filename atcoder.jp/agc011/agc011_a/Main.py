import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
ragen=range
INF=10**10
MOD=10**9+7
##############################################################################
def main():
    n,c,k=IIS()
    T=[II() for i in range(n)]
    p=0
    T.sort()
    lt=T[0]
    ans=0

    for i in range(n):
        t=T[i]
        p+=1
        if T[min(i+1,n-1)]>lt+k or p==c or i==n-1:
            ans+=1
            lt=T[min(i+1,n-1)]
            p=0
    print(ans)
if __name__=="__main__":
    main()

