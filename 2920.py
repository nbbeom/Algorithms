a= map(int,input().split())
a = list(a)
temp =0
temp1 =0
for i in range(len(a)):
    if i<len(a) and a[i] > a[i+1] :
        temp +=1
        if temp == len(a):
            print("ascending")
    elif i<len(a) and a[i] < a[i+1] :
        temp1 +=1
        if temp1 == len(a):
            print("descending")
    else : 
        print("mixed")