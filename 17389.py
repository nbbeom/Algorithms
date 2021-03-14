# n = int(input())

# s =input()
# bns=0
# score =0
# for i in range(len(list(s))):
#     if s[i] == 'O':
#         score+=i+1+bns
#         bns+=1
#     if s[i] == 'X':
#         bns=0

# print(bns+score)
n , s = input() , input()

score, bonusScore = 0,0

for idx ,OX in enumerate(s):
    if OX =='O':
        score += idx+1+bonusScore
        bonusScore+=1
    else :
        bonusScore=0

print(score)