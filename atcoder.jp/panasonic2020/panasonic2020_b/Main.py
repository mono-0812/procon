h,w=map(int,input().split())
if h==1 or w==1:
    print(1)
    exit()
from math import ceil
print(ceil(h*w/2))