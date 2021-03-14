# def teacher(n,candy):
#     tmp = [0 for i in range(n)]
#     for idx in range(n):
#         if candy[idx]%2 :
#             candy[idx]+=1
#         candy[idx]//2
#         tmp[(idx+1)% n]=candy[idx]
    
#     for idx in range(n):
#         candy[idx]+=tmp[idx]
#     return candy

# def ck(n,candy): 
#     for i in range(n):
#         if candy[i]%2 ==1:
#             candy[i] +=1
#     return len(set(candy)) == 1

# def process():
#     N, candy = int(input()),list(map(int,input().split()))
#     cnt = 0
#     while not ck(N,candy):
#         cnt+=1
#         candy = teacher(N, candy)
#     print(cnt)


# for i in range(int(input())):
#     process()

import sys ; r = sys.stdin.readline
for _ in range (int(r())):
    n, cnt = int(r()), 0
    C = [*map(int,r().split())]
    while True:
        C = [i if i % 2 == 0 else i + 1 for i in C]
        if len(set(C)) == 1:
            print(cnt)
            break
        C = [C[i]//2 + C[(i+1)%n]//2 for i in range(n)]
        cnt+=1