import heapq
def solution(scovile,k):
    heapq.heapify(scovile)
    s = scovile
    temp =0

    if k ==0 :
        return 0

    while len(scovile)>1 :
        min1 = heapq.heappop(scovile)
        min2 = heapq.heappop(scovile)
        num =min1 +min2 *2
        heapq.heappush(scovile,num)
        temp+=1

        if scovile[0]>= k:
            return temp


    return -1

scovile =[1, 2, 3, 9, 10, 12]	
k = 7
print(solution(scovile,k))