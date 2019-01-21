if __name__ == '__main__' :
    N = int(input())
    stair = [0] * (N+1)
    for i in range(1, N+1) :
        stair[i] = int(input())

    score = [0] * (N+1)
    score[1] = stair[1]
    score[2] = stair[1] + stair[2]

    for i in range(3, N+1) :
        val1 = score[i-2]
        val2 = score[i-3] + stair[i-1]
        score[i] = max(val1, val2) + stair[i]

    print(score.pop())