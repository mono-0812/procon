a,b,c,d="".join(input())
def solve(A,B,C,D):
    import itertools
    ops=("+","-")
    for op1 , op2 , op3 in itertools.product(ops,repeat=3):
        if eval(A+op1+B+op2+C+op3+D)==7:
            return A+op1+B+op2+C+op3+D+"=7"

print(solve(a,b,c,d))


    




