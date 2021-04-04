brown = 50
yellow = 22
def solution(brown, yellow):
    n = brown + yellow
    a = []
    for i in range(1,n+1):
        if n%i == 0:
            a.append(i)

    if len(a) % 2 == 0:
        b = int(len(a)/2)
        return [a[b],a[b-1]]

    else:
        b = int(len(a)/2-1/2)
        return [a[b],a[b]]

a= solution(brown,yellow)
print(a)