def solution(lottos, win_nums):
    won =[]
    l2 =lottos.copy()
    count =0
    for i in range(len(lottos)):
        if lottos[i] in win_nums :
            won.append(lottos[i])
        if lottos[i] == 0 :
            count+=1
    
    lose = lottoCount(won)
    win =lose -count
    if win == 0:
        win+=1
    answer = [win,lose]
    print(answer)


def lottoCount(won):
    if len(won)==6:
        return 1
    elif len(won)==5:
        return 2
    elif len(won)==4:
        return 3
    elif len(won)==3:
        return 4
    elif len(won)==2:
        return 5
    else : 
        return 6

solution([45, 4, 35, 20, 3, 9]	,[20, 9, 3, 45, 4, 35]	)