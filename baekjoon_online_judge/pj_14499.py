# https://www.acmicpc.net/problem/14499 주사위 굴리기

DICE = [0,0,0,0,0,0]
EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4
DIRS = [(0,1),(0,-1),(-1,0),(1,0)]


def solution(N, M, x, y, K, ARR, COMMANDS) :
	curr_x = x
	curr_y = y
	while COMMANDS :
		command = COMMANDS.pop(0)
		dx, dy = DIRS[command-1]
		if inRange(curr_x+dx, curr_y+dy, N, M) :
			curr_x += dx
			curr_y += dy
			move(command)

			if ARR[curr_x][curr_y] == 0 :
				ARR[curr_x][curr_y] = DICE[1]
			else :
				DICE[1] = ARR[curr_x][curr_y]
				ARR[curr_x][curr_y] = 0

			# print('curr_x, curr_y, command, DICE:', curr_x, curr_y, command, DICE)
			print(DICE[0])


def inRange(x, y, N, M) :
	if x>=0 and x<N and y>=0 and y<M :
		return True

	return False


def move(dir) :
	if dir == EAST :
		a, b, c, d = DICE[2], DICE[3], DICE[1], DICE[0]
		DICE[0], DICE[1], DICE[2], DICE[3] = a, b, c, d
	elif dir == WEST :
		a, b, c, d = DICE[3], DICE[2], DICE[0], DICE[1]
		DICE[0], DICE[1], DICE[2], DICE[3] = a, b, c, d
	elif dir == NORTH :
		a, b, c, d = DICE[4], DICE[5], DICE[1], DICE[0]
		DICE[0], DICE[1], DICE[4], DICE[5] = a, b, c, d
	elif dir == SOUTH :
		a, b, c, d = DICE[5], DICE[4], DICE[0], DICE[1]
		DICE[0], DICE[1], DICE[4], DICE[5] = a, b, c, d


if __name__ == '__main__' :
	N, M, x, y, K = [int(x) for x in input().split(' ')]
	ARR = [0] * N
	for i in range(N) :
		row = [int(x) for x in input().split(' ')]
		ARR[i] = row

	COMMANDS = [int(x) for x in input().split(' ')]

	solution(N, M, x, y, K, ARR, COMMANDS)

