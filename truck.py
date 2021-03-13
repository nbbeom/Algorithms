bridge_length =2
weight =10
truck_weights =[7,4,5,6]
sum = 0
answer = []
index =0
for i in range(len(truck_weights)):
    if sum + truck_weights[i] < weight:
        sum += truck_weights[i]
        index +=1  

    else : 
        answer.append(sum)
        print(sum)
        sum = 0
        sum += truck_weights[i]
    
if sum != 0:
    answer.append(sum)

print(len(answer))

temp = bridge_length*len(answer) 

print(temp)
print(index)