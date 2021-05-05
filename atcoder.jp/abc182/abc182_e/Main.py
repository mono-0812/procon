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
    h,w,n,m=IIS()
    ans=0
    F=[[0]*w for i in range(h)]
    for i in range(n):
        b,a=IIS()
        F[b-1][a-1]=1
        ans+=1
    for i in ragen(m):
        d,c=IIS()
        F[d-1][c-1]=2
    for i in range(h):
        l=False
        for j in range(w):
            if F[i][j]==1:
                l=True
            elif F[i][j]==2:
                l=False
            if l:
                if F[i][j]==0:
                    F[i][j]=3
                    ans+=1
    for i in range(h):
        l=False
        for j in range(w)[::-1]:
            if F[i][j]==1:
                l=True
            elif F[i][j]==2:
                l=False
            if l:
                if F[i][j]==0:
                    F[i][j]=3
                    ans+=1
    for j in range(w):
        l=False
        for i in range(h)[::-1]:
            if F[i][j]==1:
                l=True
            elif F[i][j]==2:
                l=False
            if l:
                if F[i][j]==0:
                    F[i][j]=3
                    ans+=1
    for j in range(w):
        l=False
        for i in range(h):
            if F[i][j]==1:
                l=True
            elif F[i][j]==2:
                l=False
            if l:
                if F[i][j]==0:
                    F[i][j]=3
                    ans+=1
    print(ans)
if __name__=="__main__":
    main()