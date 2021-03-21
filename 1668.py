def asn(arr):
    now = arr[0]
    result =1
    for i in range(1,len(arr)):
        if now < arr[i]:
            result+=1
            now = arr[i]
    return result

t = int(input())
a = [int(input()) for _ in range(t)]

print(asn(a))
a.reverse()
print(asn(a))