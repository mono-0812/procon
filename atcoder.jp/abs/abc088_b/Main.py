#-*- coding:utf-8 -*-
num = int(input())
li = list(map(int, input().split()))
A = 0
B = 0
c = num
for i in range(num):
	if c >= 1:
		A = A + max(li)
		li.remove(max(li))
		c = c - 1
		if c >= 1:
			B = B + max(li)
			li.remove(max(li))
			c = c - 1	
print(A - B)