n,l,k = map(int, input().split())
# sub1,sub2 =[],[]
# for i in range(n):
#     s1,s2 = map(int, input().split())
#     sub1.append(s1)
#     sub2.append(s2)

# temp2 =0
# temp =0
# for i in range(k):
#     if sub2[i]>l:
#         if sub1[i] <= l:
#             temp2+=1
#     else :
#         temp +=1

# if temp2+temp >= k :
#     temp = k -temp2
#     print(temp2*100+temp*140)
# else : 
#     print(temp2*100+temp*140)
hard , easy = 0,0
for i in range(n):
    sub1, sub2 = map(int,input().split())
    if sub2 <=l :
        hard +=1
    elif sub1 <=l:
        easy+=1

ans = min(hard, k)*140
if hard < k:
    ans+=max(k-hard, easy) *100

print(ans)