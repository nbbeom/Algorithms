array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
temp =[]
for i in range (len(commands)):
    ary2 =array[commands[i][0]-1 :commands[i][1]]
    ary2 =sorted(ary2)
    
    temp.append(ary2[commands[i][2]-1])
    print(temp)