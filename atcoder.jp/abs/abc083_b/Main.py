#-*- coding:utf-8 -*-
N,A,B = map(int,input().split())
q = 0
w = 0
v = 0
total = 0
for i in range(N+1):
	v = 0
	i = str(i)
	for c in i:
		v += int(c)
	if v <= B and v >= A:
		total = total + int(i)
print(total)