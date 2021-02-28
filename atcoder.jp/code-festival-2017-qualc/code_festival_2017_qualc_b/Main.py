n=int(input())
X=list(map(int,input().split()))
x=1
ans=0
def solve(Y,num):
    if num==n:
        val=1
        for i in Y:
            val*=i

        if val%2==0:
            global ans
            ans+=1
        return 0
    solve(Y+[X[num]+1],num+1)
    solve(Y+[X[num]],num+1)
    solve(Y+[X[num]-1],num+1)
    return 0
solve([],0)
print(ans)