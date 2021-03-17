# z :0,0 기준으로 x y 의 숫자
n , r, c =map(int, input().split())

def Z(n,x,y):
    if n == 1:
        return 0
    n //=2
    for i in range(2):
        for j in range(2):
            if x< n*(i+1) and y < n*(j+1):
                return (i*2+j)*n*n+Z(n,x-n*i,y-n*j)



print(Z(2**n,r,c))