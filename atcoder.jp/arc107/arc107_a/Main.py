a,b,c=map(int,input().split())
def solve(N):
    return N*(1+N)
print(solve(a)*solve(b)*solve(c)//8%998244353)