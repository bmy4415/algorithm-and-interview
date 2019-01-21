# https://www.acmicpc.net/problem/15684 사다리 문제

DEBUG = True


import itertools

def solution(ARR, N, M, H) :
    lines = []

    # 입력으로 주어진 선 외의 모든 선은 후보임
    for i in range(1, N) :
        for j in range(1, H+1) :
            if ARR[i][j] == 0 :
                lines.append((i, j))

    if DEBUG :
        print('----------------------------')
        print('ARR')
        for row in ARR :
            print(row)

        print('lines: ', lines)

    
    # 하나도 추가하지 않았을 때 확인
    result = check(ARR)
    if result == True :
        print('success: ', 0)
        return


    for i in range(1, 4) :
        combinations = itertools.combinations(lines, i)

        for comb in combinations :
            if DEBUG :
                print(list(comb))

            # 해당 comb에 대하여 결과 확인


            if DEBUG :
                print('변경 전 ARR')
                for row in ARR :
                    print(row)



            restore = {} # 복구용도 dic
            # ARR 변경
            for line in comb :
                a, b = line
                restore[(a, b)] = ARR[a][b]
                restore[(a+1, b)] = ARR[a+1][b]

                if DEBUG :
                    print('origin: ', ARR[a][b], ARR[a+1][b])
                    print('restore: ', restore[(a, b)], restore[(a+1, b)])

                ARR[a][b] = 2
                ARR[a+1][b] = 1


            # 조건 만족하는지 check
            result = check(ARR)
            if result == True :
                print('success: ', i)
                return


            # ARR 복구
            for line in comb :
                a, b = line
                ARR[a][b] = restore[(a, b)]
                ARR[a+1][b] = restore[(a+1, b)]


            if DEBUG :
                print('변경 후 ARR')
                for row in ARR :
                    print(row)


    print('fail: ', -1)
    return


# 문제의 조건 만족하는지 확인
# i번째 세로선의 결과 -> i
# 연속하여 두개의 줄은 없음
def check(ARR) :
    # 연속한 2개의 줄 확인
    for i in range(1, N) :
        for j in range(1, H+1) :
            if ARR[i][j] != 0 and ARR[i][j] == ARR[i+1][j] :
                if DEBUG :
                    print('not correct graph')
                return False

    # i번째 세로선의 결과 확인
    for i in range(1, N+1) :
        result = go(ARR, i)
        if i != result :
            if DEBUG :
                print('i: ', i, ' result: ', result)
            return False


    return True
    

# n번째 세로선의 결과값을 확인
def go(ARR, n) :
    curr_n = n

    for curr_h in range(1, N+1) :
        if ARR[curr_n][curr_h] == 0 :
            continue
        elif ARR[curr_n][curr_h] == 1 :
            # 왼쪽으로 이동
            curr_n -= 1
        elif ARR[curr_n][curr_h] == 2 :
            # 오른쪽으로 이동
            curr_n += 1

    return curr_n



if __name__ == '__main__' :
    N, M, H = [int(x) for x in input().split(' ')]
    ARR = [[0 for _ in range(H+1)] for _ in range(N+1)]

    for _ in range(M) :
        a, b = [int(x) for x in input().split(' ')]
        ARR[b][a] = 2 # 오른쪽으로 이동 가능
        ARR[b+1][a] = 1 # 왼쪽으로 이동 가능


    print('최초 ARR')
    for row in ARR :
        print(row)


    solution(ARR, N, M, H)
    

