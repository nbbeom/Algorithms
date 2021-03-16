n,A = input(),{i: 1 for i in map(int , input().split())}
m = int(input())

# for i in range(m):
#     if a[i] in x :
#         print(1)
#     else :
#         print(0)

for i in list(map(int,input().split())):
    print(A.get(i,0))
    #dict에서 get 을 사용하면 등록이 안된 키여도 디폴트 값 0 을 출력
