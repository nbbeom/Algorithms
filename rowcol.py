def solution(rows, columns, queries):
    a =[[0 for col in range(columns)] for row in range(rows)]
    count=1
    for i in range(rows):
        for j in range(columns):
            a[i][j]=count
            count+=1
    
    print(a)

    for i in range(len(queries)):
        x = queries[i][0],queries[i][2]
        y = queries[i][1],queries[i][3]
        temp =[]
        
        print(temp)
            
solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])