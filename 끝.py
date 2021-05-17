
def solution(n, words):

    wrongNumber =[]
    for i in range(len(words)):
        if i == len(words) :
            continue
        else :
            if words[i+1][0] == words[i][-1]:
                wrongNumber.append(i)
    print(i)
    return wrongNumber
n =3
words =["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	
print(solution(n,words))