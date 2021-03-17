lst = sorted(list(map(int, input().split())))

if len(set(lst)) == 1:
    print(lst[0]*1000+10000)
elif len(set(lst)) == 2:
    print(1000 + lst[1]*100)
else :
    print(lst[2]*100)