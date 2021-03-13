input = __import__('sys').stdin.readline

def add(X):
    dp = []
    take = []
    for i in range(n):
        x = A[i] + X
        val = min((x, 1), (0, 0))
        if i >= 1: 
            val = min(val, (dp[-1], take[-1]))
        if i >= 2: 
            val = min(val, (dp[-2]+x, take[-2]+1))
        dp.append(val[0])
        take.append(val[1])
    return (dp[-1], take[-1])

n, k = map(int,input().split())
s = [int(input()) for i in range(n)]
A = [s[i+1]-s[i] for i in range(n-1)]
n-= 1

l = -10**9; r = 0
while l <= r:
    mid = (l+r)//2
    dp, take = add(mid)
    if take <= k: ans = dp-k*mid; r = mid-1
    else: l = mid+1
print(ans)