answers= [1, 3, 2, 4, 2]

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

cnt =[0,0,0]
temp =[]
for i , ans in enumerate(answers):
    if ans == arr1[i%5]:
        cnt[0]+=1
    if ans == arr2[i%8]:
        cnt[1]+=1
    if ans == arr3[i%10]:
        cnt[2]+=1

if cnt[0] > cnt[1] :
    if cnt[0]> cnt[2]:
        temp.append(1)
    elif cnt[0]==cnt[2]:
        temp.append(1)
        temp.append(3)
if cnt[0] < cnt[1]:
    if cnt[1]> cnt[2]:
        temp.append(2)
    elif cnt[1]==cnt[2]:
        temp.append(2)
        temp.append(3)
if cnt[0] == cnt[1]:
    if cnt[1]> cnt[2]:
        temp.append(1)
        temp.append(2)
    elif cnt[1]==cnt[2]:
        temp.append(1)
        temp.append(2)
        temp.append(3)

temp.sort()


print(temp)