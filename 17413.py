clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    clothes = dict(clothes)
    a = []
    for i in clothes:
        a.append(clothes[i])

    if len(set(a)) == 1:
        return len(a)
    elif len(set(a)) == len(a)-1 :
        return len(a)+len(set(a))
    else :
        l = len(a) - len(set(a))
        r = len(a) - l
        return len(a)+l*r

print(solution(clothes))