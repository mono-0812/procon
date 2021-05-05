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
    n,m,k=IIS()
    for i in range(n+1):
        for j in range(m+1):
            if i*(m-j)+j*(n-i)==k:
                print("Yes")
                exit()
    print("No")
if __name__=="__main__":
    main()

