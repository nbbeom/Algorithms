import collections
from collections import Counter
def BFS(begin, target, words,answer):
    if target==begin:
        return answer
    else:
        #print (target,begin)
        for item in words:
            flag=0
            len_s=len(list((Counter(target) - Counter(item)).elements()))
            len_s2=len(list((Counter(target) - Counter(begin)).elements()))

            # if (len_s==1 and target==item)
            if (len_s<=len_s2 and len_s2!=1) or (len_s2==1 and target==item):
                #print (item)
                for ch,ch_b in zip(item,begin):
                    if ch!=ch_b:
                        flag=flag+1
                        if flag==2:
                            break
                if flag==1:
                    begin=item
                    words.remove(item)
                    # print (words)
                    answer=BFS(begin, target, words,answer)
                    answer=answer+1
                    break
        return answer

def solution(begin, target, words):
    answer = 0
    if target in words:
        answer=BFS(begin, target, words,answer)
    else:
        pass
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin,target,words)