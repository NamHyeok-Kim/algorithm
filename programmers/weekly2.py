def solution(scores):
    answer = ""

    for i in range(len(scores[0])):
        r = len(scores[0])
        selfScore = scores[i][i]
        sums = 0
        maxScore = 0
        minScore = 101
        for j in range(r):
            if scores[j][i] > maxScore: maxScore = scores[j][i]
            if scores[j][i] < minScore: minScore = scores[j][i]
            sums += scores[j][i]

        if(len(list(filter(lambda e: scores[j][e] == maxScore, range(len(scores[i]))))) == 1 or len(list(filter(lambda e: scores[j][e] == minScore, range(len(scores[i]))))) == 1):
            if selfScore == maxScore or selfScore == minScore:
                sums -= selfScore
                r -= 1
        a = sums // r
        if a >= 90: answer += "A"
        elif 90 > a >= 80: answer += "B"
        elif 80 > a >= 70: answer += "C"
        elif 70 > a >= 50: answer += "D"
        else: answer += "F"

    return answer

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])