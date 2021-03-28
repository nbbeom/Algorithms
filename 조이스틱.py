def solution(number, k):
    
    data =[]
    number = list(number)
    print(number)

    for i in range(len(number)):
        for j in range(len(number)-1):
            a= number.copy()
            a.remove(a[i])
            a.remove(a[j])
            a =''.join(a)
            data.append(int(a))
            
    print(data)

num = "1924"
k =2
solution(num,k)