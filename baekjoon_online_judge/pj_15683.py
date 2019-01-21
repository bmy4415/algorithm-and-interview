# https://www.acmicpc.net/problem/15683, 감시
from itertools import product

DEBUG = False
UNSEEN = 0
SEEN = -1
WALL = 6


def solution(ARR, N, M) :

	cctvs = []
	for i in range(N) :
		for j in range(M) :
			if ARR[i][j] >= 1 and ARR[i][j] <= 5:
				cctvs.append((i, j, ARR[i][j]))

	combinations = findAllCombinations(cctvs)

	# if DEBUG :
	# 	for comb in combinations :
	# 		print(comb)

	MIN = N*M
	for comb in combinations :
		num_unseen = calculateUnseen(ARR, comb)

		if num_unseen < MIN :
			MIN = num_unseen

	print(MIN)


# 해당 카메라 방향 조합에 대하여 감시 불가능한 구역의 숫자를 return
def calculateUnseen(map, case) :
	new_map = [row[:] for row in map]
	for cctv in case :
		x, y, type, dir = cctv

		if type == 1 :
			if dir == 0 :
				up(new_map, x, y)
			elif dir == 1 :
				right(new_map, x, y)
			elif dir == 2 :
				down(new_map, x, y)
			elif dir == 3 :
				left(new_map, x, y)

		elif type == 2 :
			if dir == 0 :
				left(new_map, x, y)
				right(new_map, x, y)
			elif dir == 1 :
				up(new_map, x, y)
				down(new_map, x, y)

		elif type == 3 :
			if dir == 0 :
				up(new_map, x, y)
				right(new_map, x, y)
			elif dir == 1 :
				down(new_map, x, y)
				right(new_map, x, y)
			elif dir == 2 :
				down(new_map, x, y)
				left(new_map, x, y)
			elif dir == 3 :
				up(new_map, x, y)
				left(new_map, x, y)

		elif type == 4 :
			if dir == 0 :
				up(new_map, x, y)
				left(new_map, x, y)
				right(new_map, x, y)
			elif dir == 1 :
				up(new_map, x, y)
				down(new_map, x, y)
				right(new_map, x, y)
			elif dir == 2 :
				down(new_map, x, y)
				left(new_map, x, y)
				right(new_map, x, y)
			elif dir == 3 :
				up(new_map, x, y)
				down(new_map, x, y)
				left(new_map, x, y)

		elif type == 5 :
			up(new_map, x, y)
			down(new_map, x, y)
			left(new_map, x, y)
			right(new_map, x, y)


	# of unseen
	count = 0
	for i in range(N) :
		for j in range(M) :
			if new_map[i][j] == UNSEEN :
				count += 1


	if DEBUG :
		print('-------------------------')
		for row in new_map :
			print(row)
		print('case, num_unseen: ', case, count)
	return count

def up(map, x, y) :
	while(x >= 0 and map[x][y] != WALL) :
		map[x][y] = SEEN
		x -= 1

def down(map, x, y) :
	while(x < N and map[x][y] != WALL) :
		map[x][y] = SEEN
		x += 1

def left(map, x, y) :
	while(y >= 0 and map[x][y] != WALL) :
		map[x][y] = SEEN
		y -= 1

def right(map, x, y) :
	while(y < M and map[x][y] != WALL) :
		 map[x][y] = SEEN
		 y += 1


def findAllCombinations(cctvs) :
	temp = list((map(case, cctvs)))
	return product(*temp)

def case(obj) :
	x, y, type = obj
	if type == 1 or type == 3 or type == 4 :
		return [
			(x, y, type, 0), # x, y, type, direction
			(x, y, type, 1),
			(x, y, type, 2),
			(x, y, type, 3),
		]
	elif type == 2 :
		return [
			(x, y, type, 0), # x, y, type, direction
			(x, y, type, 1),
		]
	elif type == 5 :
		return [(x, y, type, 0)]



if __name__ == '__main__' :
	n, m = [int(x) for x in input().split(' ')]
	N = n
	M = m

	ARR = []

	for _ in range(N) :
		row = [int(x) for x in input().split(' ')]
		ARR.append(row)

	solution(ARR, N, M)