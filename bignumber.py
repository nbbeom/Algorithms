# a =[6, 10, 2]
b=[222,9,3]
temp=[]

for i in range(len(b)):
    a = str(b[i])
    c = str(b[i+1])
    if int(a+c) >int(c+a):
        print(a+c) 



