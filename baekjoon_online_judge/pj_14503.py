# https://www.acmicpc.net/problem/14503

DEBUG = False


def getEast(coor, N, M, x, y) :
    if y+1 < M : return (x, y+1, coor[x][y+1])
    else : return (x, y+1, 1)

def getWest(coor, N, M, x, y) :
    if y-1 >= 0 : return (x, y-1, coor[x][y-1])
    else : return (x, y-1, 1)

def getSouth(coor, N, M, x, y) :
    if x+1 < N : return (x+1, y, coor[x+1][y])
    else : return (x+1, y, 1)

def getNorth(coor, N, M, x, y) :
    if x-1 >= 0 : return (x-1, y, coor[x-1][y])
    else : return (x-1, y, 1)

def solution(coor, N, M, r, c, d) :
    count = 0
    arr = []

    arr.append((r, c, d))

    while(len(arr) > 0) :
        curr_x, curr_y, curr_d = arr.pop()
        if (coor[curr_x][curr_y] == 0) :
            coor[curr_x][curr_y] = 2 # 청소완료 = 2
            count += 1


        # debug print
        if DEBUG : 
            print('------------------------')
            print('curr_x, curr_y, curr_d, count', curr_x, curr_y, curr_d, count)
            for row in coor :
                print(row)


        

        directions = [
            getNorth(coor, N, M, curr_x, curr_y),
            getEast(coor, N, M, curr_x, curr_y),
            getSouth(coor, N, M, curr_x, curr_y),
            getWest(coor, N, M, curr_x, curr_y),
        ]

        rot1 = directions[(curr_d-1) % 4]
        rot2 = directions[(curr_d-2) % 4]
        rot3 = directions[(curr_d-3) % 4]
        rot4 = directions[(curr_d-4) % 4]

        # debug print
        if DEBUG : 
            print('ro1: ', rot1)
            print('ro2: ', rot2)
            print('ro3: ', rot3)
            print('ro4: ', rot4)

        if rot1[2] == 0 :
            # 청소 가능
            next_d = (curr_d-1) % 4 # 회전
            arr.append((rot1[0], rot1[1], next_d)) # 한칸 이동
            continue

        if rot2[2] == 0 :
            next_d = (curr_d-2) % 4 # 회전
            arr.append((rot2[0], rot2[1], next_d))
            continue

        if rot3[2] == 0 :
            next_d = (curr_d-3) % 4 # 회전
            arr.append((rot3[0], rot3[1], next_d))
            continue

        if rot4[2] == 0 :
            next_d = (curr_d-4) % 4 # 회전
            arr.append((rot4[0], rot4[1], next_d))
            continue


        # 청소 가능한 방향 없음

        if rot2[2] == 1 :
            # 벽 -> 중지
            break

        # 방향유지, 후진 1칸
        elif rot2[2] == 2 :
            arr.append((rot2[0], rot2[1], curr_d))

    print(count)


if __name__ == '__main__' :
    N, M = [int(x) for x in input().split(' ')]
    r, c, d = [int(x) for x in input().split(' ')]

    COORDINATE = []
    for i in range(N) :
        row = [int(x) for x in input().split(' ')]
        COORDINATE.append(row)


    #  print(N, M)
    #  print(r, c, d)
    #  print(COORDINATE)

    solution(COORDINATE, N, M, r, c, d)
