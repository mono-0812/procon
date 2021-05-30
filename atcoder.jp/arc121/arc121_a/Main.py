import collections
import itertools
import math
import decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
class max_manhattan_distance():
    #O(1)
    def __init__(self):
        self.coordinate_list1=[]
        self.coordinate_list2=[]
    #O(1)
    def add_coordinate(self,X,Y):
        self.coordinate_list1.append(X)
        self.coordinate_list2.append(Y)
    #O(NlogN)
    def get_max_manhattan_distance(self):
        self.coordinate_list1.sort()
        self.coordinate_list2.sort()
        val=0
        if self.coordinate_list1[-1]-self.coordinate_list1[0]==self.coordinate_list2[-1]-self.coordinate_list2[0]:
            val=-1
        return sorted([self.coordinate_list1[-1]-self.coordinate_list1[1],self.coordinate_list2[-1]-self.coordinate_list2[1],self.coordinate_list2[-2]-self.coordinate_list2[0],self.coordinate_list1[-2]-self.coordinate_list1[0],self.coordinate_list1[-1]-self.coordinate_list1[0],self.coordinate_list2[-1]-self.coordinate_list2[0]])[-2+val]
n=II()
mh=max_manhattan_distance()
for i in range(n):
    x,y=IIS()
    mh.add_coordinate(x,y)
print(mh.get_max_manhattan_distance())