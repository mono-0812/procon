n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
val = 0
cnt = 0
ans = 0
while cnt != n:
	val = val + a[cnt] * b[cnt]
	cnt += 1
if val == 0:
	ans = "Yes"
else:
  	ans = "No"
print(ans)