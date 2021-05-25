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
        self.coordinate_list1.append(X+Y)
        self.coordinate_list2.append(X-Y)
    #O(NlogN)
    def get_max_manhattan_distance(self):
        self.coordinate_list1.sort()
        self.coordinate_list2.sort()
        return max(self.coordinate_list1[-1]-self.coordinate_list1[0],self.coordinate_list2[-1]-self.coordinate_list2[0])
mh=max_manhattan_distance()
for i in range(II()):
    x,y=IIS()
    mh.add_coordinate(x,y)
print(mh.get_max_manhattan_distance())
