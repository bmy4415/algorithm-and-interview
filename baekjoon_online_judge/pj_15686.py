# https://www.acmicpc.net/problem/15686, 치킨 배달

import itertools

def getChickenDistance(HOMES, comb) :
	result = 0

	for home in HOMES :
		distances = list(map(lambda x: abs(x[0] - home[0]) + abs(x[1] - home[1]), list(comb)))
		min_distance = min(distances)
		result += min_distance

	return result



def solution(HOMES, CHICKENS, N, M) :
	COMBINATIONS = itertools.combinations(CHICKENS, M)
	MIN = pow(50, 4)

	for comb in COMBINATIONS :
		chicken_distance = getChickenDistance(HOMES, comb)
		if chicken_distance < MIN :
			MIN = chicken_distance


	print(MIN)



if __name__ == '__main__' :
	N, M = [int(x) for x in input().split(' ')]

	HOMES = []
	CHICKENS = []
	for n in range(1, N+1) :
		row = [int(x) for x in input().split(' ')]

		for i, value in enumerate(row) :
			if (row[i] == 1) : HOMES.append((n, i+1))
			elif (row[i] == 2) : CHICKENS.append((n, i+1))


	solution(HOMES, CHICKENS, N, M)