# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu 보호 필름

from itertools import combinations, product
import time

A = 0
B = 1

# ARR의 index번째 row에 which 약품을 한 후
# return (성공여부, 결과arr)
def simulate(D, W, K, ARR, comb, ABs, length) :
	arr = [row[:] for row in ARR]
	for AB in ABs :
		for i in range(length) :
			index = comb[i]
			which = AB[i]
			row = [which] * W
			arr[index] = row

		# print('comb, ABs:', comb, ABs)
		# for row in arr :
		# 	print(row)
		result = check(D, W, K, arr)
		if result :
			return True

	return False



# 연속한 K개의 cell이 있는지 확인
def check(D, W, K, arr) :
	for j in range(W) :
		count = 1
		for i in range(D-1) :
			if arr[i][j] == arr[i+1][j] :
				count += 1
			else :
				count = 1

			if count == K :
				break

		if count != K :
			return False

	return True


# return 약품 투입 횟수
def solve(D, W, K, ARR) :
	if check(D, W, K, ARR) :
		return 0

	indexes = range(D)
	lengths = range(1,K)
	for length in lengths :
		# print('D, length:', D, length)
		all_combinations = combinations(indexes, length)
		ABs = list(product([0,1], repeat=length))
		for comb in all_combinations :
			result = simulate(D, W, K, ARR, comb, ABs, length)
			if result :
				return length

	return K




if __name__ == '__main__' :
	T = int(input())
	problems = [0] * T
	for i in range(T) :
		D, W, K = [int(x) for x in input().split(' ')[:3]]
		arr = [0] * D
		for j in range(D) :
			row = [int(x) for x in input().split(' ')[:W]]
			arr[j] = row

		problems[i] = (D, W, K, arr)


	for i, problem in enumerate(problems) :
		D, W, K, arr = problem
		start = time.time()
		result = solve(D, W, K, arr)
		end = time.time()
		print('#{} {}'.format(i+1, result))
		print(end-start)

