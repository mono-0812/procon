n=int(input())
mod=10**9+7
if n<2:
    print(n*(n-1)%mod)
else:
    print((10**n-2*9**n+8**n)%mod)