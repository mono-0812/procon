n=int(input())
st=set()
import random
li=[(3,3),(3,-3),(-3,3),(-3,-3)]
for i in range(n):
    x,y,r=map(int,input().split())
    for i,j in li:
        if (x+i,y+j) in st:
            continue
        if 0<=x<=10000 and 0<=y<=10000 and 0<=x+i<=10000 and 0<=y+j<=10000:
            print(x,y,x+1,y+1)
            st.add((x,y))
            st.add((x+i,y))
            st.add((x,y+j))
            st.add((x+i,y+j))
            break