# https://www.acmicpc.net/problem/14890 경사로

def solution(N, L, arr) :
	count = 0
	for i in range(N) :
		row = arr[i]
		col = [temp[i] for temp in arr]
		# print('row: ', row)
		r1 = check_road(N, L, row)
		# print('result: ', r1)
		# print('col: ', col)
		r2 = check_road(N, L, col)
		# print('result: ', r2)
		if check_road(N, L, row) :
			count += 1
		if check_road(N, L, col) :
			count += 1


	print(count)

def check_road(N, L, road) :
	arr = list(map(lambda x: [x, 0], road)) # 경사로 여부 추가

	i = 0
	while i < N-1 :
		# print('arr, i:', arr, i)
		if abs(arr[i][0] - arr[i+1][0]) >= 2 :
			return False

		if arr[i][0] == arr[i+1][0] :
			i += 1
			continue

		# 오른쪽에 경사로 설치
		if arr[i][0] - arr[i+1][0] == 1 :
			# (i+1)~(i+L)이 모두 같은 높이인지 확인, 아직 확인하지 않은 영역이므로 경사로는 설치 가능
			if i+L >= N :
				return False

			j = i+1
			while j <= i+L-1 :
				if arr[j][0] != arr[j+1][0] :
					return False

				j += 1

			# 경사로 설치
			for j in range(i+1, i+L+1) :
				arr[j][1] = 1

			# (i+L)번째 부터 다시 확인
			i = i+L
			continue

		# 왼쪽에 경사로 설치
		if arr[i][0] - arr[i+1][0] == -1 :
			# 경사로 설치 가능한지 확인
			# 높이는 확인하지 않아도됨 -> 이미 경사로를 설치하면서 왔으면 다를 수 있음
			if i-L+1 < 0 :
				return False

			j = i-L+1
			while j <= i :
				if arr[j][1] == 1 or arr[j+1][1] == 1:
					return False

				j += 1

			# 경사로 설치
			for j in range(i-L+1, i+1) :
				arr[j][1] = 1

			# (i+1)번째 부터 다시 확인
			i += 1
			continue

	return True


if __name__ == '__main__' :
	N, L = [int(x) for x in input().split(' ')]
	arr = [0] * N
	for i in range(N) :
		row = [int(x) for x in input().split(' ')]
		arr[i] = row

	solution(N, L, arr)

