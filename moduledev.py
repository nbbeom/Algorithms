from collections import deque


def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    # 모든 작업을 배포했을 때 종료
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        temp = 0
        while progresses and progresses[0] > 100:
            progresses.popleft()
            speeds.popleft()
            temp += 1

        if temp >= 1:
            answer.append(temp)

    return answer