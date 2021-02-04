n,k=map(int,input().split())
print(min(abs(n-(n//k)*k),abs(n-(n//k+1)*k)))