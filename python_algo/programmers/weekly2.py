def solution(scores):
    answer = ""
    r = len(scores[0])
    for i in range(r):
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