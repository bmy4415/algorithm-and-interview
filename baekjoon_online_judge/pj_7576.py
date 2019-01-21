# https://www.acmicpc.net/problem/7576

def solution(ARR, N, M) :
    count = 0
    arr = []
    
    for n in range(N) :
        for m in range(M) :
            if (ARR[n][m] == 1) :
                arr.append([n, m])

    while(len(arr) != 0) :
        #  print('before: ', ARR)
        #  print('coordinate: ', arr)
        count += 1
        temp_arr = arr.copy()
        arr.clear()

        for coordinate in temp_arr :
            n, m = coordinate
            # 왼쪽
            if (m-1 >= 0 and ARR[n][m-1] == 0) :
                ARR[n][m-1] = 1
                arr.append([n, m-1])

            # 오른쪽
            if (m+1 < M and ARR[n][m+1] == 0) :
                ARR[n][m+1] = 1
                arr.append([n, m+1])

            # 위
            if (n-1 >= 0 and ARR[n-1][m] == 0) :
                ARR[n-1][m] = 1
                arr.append([n-1, m])

            # 아래
            if (n+1 < N and ARR[n+1][m] == 0) :
                ARR[n+1][m] = 1
                arr.append([n+1, m])

        #  print('after: ', ARR)


    for n in range(N) :
        for m in range(M) :
            if ARR[n][m] == 0 :
                print(-1)
                return

    print(count-1)



if __name__ == '__main__' :
    M, N = [int(x) for x in input().split(' ')]
    ARR = []

    for x in range(N) :
        row = [int(y) for y in input().split(' ')]
        ARR.append(row)


    solution(ARR, N, M)


