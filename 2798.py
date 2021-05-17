n,m = list(map(int,input().split(' ')))
data = list(map(int,input().split(' ')))

result =0
leng = len(data)

count =0
for i in range(0,leng):
    for j in range(i+1,leng):
        for k in range(j+1, leng):
            sum_val = data[i]+data[j]+data[k]
            if sum_val<=m:
                result = max(result,sum_val)

print(result)
