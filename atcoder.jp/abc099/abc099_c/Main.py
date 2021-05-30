import collections
import itertools
import math
import decimal
import bisect
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n=II()
li=[]
def min_num_part_sum(a, A):
    # 初期化
    N = len(a)
    inf = float("inf")
    dp = [[inf for i in range(A + 1)] for j in range(N + 1)]
    dp[0][0] = 0

    # DP
    for i in range(N):
        for j in range(A + 1):
            if a[i] <= j:  # i+1番目の数字a[i]を足せるかも
                dp[i + 1][j] = min(dp[i][j - a[i]] + 1, dp[i][j])
            else:  # 入る可能性はない
                dp[i + 1][j] = dp[i][j]
    return dp[N][A]
val=1
while n>=val:
    if n<val:
        continue
    for i in range(6):
        li.append(val)
    val*=6
li.pop()
val=1
while n>=val:
    if n<val:
        continue
    v=val
    for i in range(9):
        li.append(val)
    val*=9
li.pop()
li.append(1)
li.sort()
print(min_num_part_sum(li,n))