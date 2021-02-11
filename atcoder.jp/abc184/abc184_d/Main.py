A,B,C=map(int,input().split())
dp=[[[0]*101 for i in range(101)]for i in range(101)]
def f(a,b,c):
    if dp[a][b][c]!=0:
        return(dp[a][b][c])
    if a==100 or b==100 or c==100:
        return 0
    ans = 0
    n = a+b+c
    ans += (f(a+1,b,c)+1)*a/n
    ans+= (f(a,b+1,c)+1)*b/n
    ans+=(f(a,b,c+1)+1)*c/n
    dp[a][b][c]=ans
    return ans
print(f(A,B,C))