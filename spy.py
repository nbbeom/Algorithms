clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
#clothes = [["crow_mask", "a"], ["blue_sunglasses", "a"], ["smoky_makeup", "face"]]
from collections import Counter
def sol(clothes):
    clothe_list =[]
    for cloth in clothes:
        clothe_list.append(cloth[1])
    answer = Counter(clothe_list)
    print(answer)
    if len(answer)==1:
        return list(answer.values())[0]

    else :
        ret = 1
        for v in list(answer.values()):
            ret*= (v+1)
        return ret-1

sol(clothes)
