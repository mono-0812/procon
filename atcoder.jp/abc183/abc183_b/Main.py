sx,sym,gx,gy = map(int,input().split())

sy = sym * -1
mx = gx - sx
my = gy - sy
a = my / mx
b = gy-a*gx
ans = (0-b)/a
print(ans)