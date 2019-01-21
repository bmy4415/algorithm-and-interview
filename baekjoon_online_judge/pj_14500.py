def solution(coordinate, N, M) :
	values = []

	for n in range(N) :
		for m in range(M) :
			# 0 0 0 0
			if (n+3 < N) :
				values.append(coordinate[n][m] + coordinate[n+1][m] + coordinate[n+2][m] + coordinate[n+3][m])

			if (m+3 < M) :
				values.append(coordinate[n][m] + coordinate[n][m+1] + coordinate[n][m+2] + coordinate[n][m+3])

			# 0 0
			# 0 0
			if (n+1 < N and m+1 < M) :
				values.append(coordinate[n][m] + coordinate[n+1][m] + coordinate[n][m+1] + coordinate[n+1][m+1])


			# 0 0 0
			#     0
			if (n+2 < N and m+1 < M) :
				values.append(coordinate[n][m] + coordinate[n+1][m] + coordinate[n+2][m] + coordinate[n+2][m+1])

			if (n+1 < N and m-2 >= 0) :
				values.append(coordinate[n][m] + coordinate[n][m-1] + coordinate[n][m-2] + coordinate[n+1][m-2])

			if (n-2 >= 0 and m-1 >= 0) :
				values.append(coordinate[n][m] + coordinate[n-1][m] + coordinate[n-2][m] + coordinate[n-2][m-1])

			if (n-1 >= 0 and m+2 < M) :
				values.append(coordinate[n][m] + coordinate[n][m+1] + coordinate[n][m+2] + coordinate[n-1][m+2])

			if (n+2 < N and m-1 >= 0) :
				values.append(coordinate[n][m] + coordinate[n+1][m] + coordinate[n+2][m] + coordinate[n+2][m-1])

			if (n+1 < N and m+2 < M) :
				values.append(coordinate[n][m] + coordinate[n][m+1] + coordinate[n][m+2] + coordinate[n+1][m+2])

			if (n-2 >= 0 and m+1 < M) :
				values.append(coordinate[n][m] + coordinate[n-1][m] + coordinate[n-2][m] + coordinate[n-2][m+1])

			if (n-1 >= 0 and m-2 >= 0) :
				values.append(coordinate[n][m] + coordinate[n][m-1] + coordinate[n][m-2] + coordinate[n-1][m-2])

			# 0 0
			#   0 0
			if (n+2 < N and m+1 < M) :
				values.append(coordinate[n][m] + coordinate[n+1][m] + coordinate[n+1][m+1] + coordinate[n+2][m+1])

			if (n+1 < N and m-2 >= 0) :
				values.append(coordinate[n][m] + coordinate[n][m-1] + coordinate[n+1][m-1] + coordinate[n+1][m-2])

			if (n-2 >= 0 and m-1 >= 0) :
				values.append(coordinate[n][m] + coordinate[n-1][m] + coordinate[n-1][m-1] + coordinate[n-2][m-1])

			if (n-1 >= 0 and m+2 < M) :
				values.append(coordinate[n][m] + coordinate[n][m+1] + coordinate[n-1][m+1] + coordinate[n-1][m+2])

			if (n+2 < N and m-1 >= 0) :
				values.append(coordinate[n][m] + coordinate[n+1][m] + coordinate[n+1][m-1] + coordinate[n+2][m-1])

			if (n+1 < N and m+2 < M) :
				values.append(coordinate[n][m] + coordinate[n][m+1] + coordinate[n+1][m+1] + coordinate[n+1][m+2])

			if (n-2 >= 0 and m+1 < M) :
				values.append(coordinate[n][m] + coordinate[n-1][m] + coordinate[n-1][m+1] + coordinate[n-2][m+1])

			if (n-1 >= 0 and m-2 >= 0) :
				values.append(coordinate[n][m] + coordinate[n][m-1] + coordinate[n-1][m-1] + coordinate[n-1][m-2])


			# 0 0 0
			#   0
			if (n+1 < N and m+2 < M) :
				values.append(coordinate[n][m] + coordinate[n][m+1] + coordinate[n+1][m+1] + coordinate[n][m+2])

			if (n+2 < N and m-1 >= 0) :
				values.append(coordinate[n][m] + coordinate[n+1][m] + coordinate[n+2][m] + coordinate[n+1][m-1])

			if (n-1 >= 0 and m-2 >= 0) :
				values.append(coordinate[n][m] + coordinate[n][m-1] + coordinate[n][m-2] + coordinate[n-1][m-1])

			if (n-2 >= 0 and m+1 < M) :
				values.append(coordinate[n][m] + coordinate[n-1][m] + coordinate[n-2][m] + coordinate[n-1][m+1])


	print(max(values))


if __name__ == '__main__' :
	N, M = [int(x) for x in input().split(' ')]

	COORDINATE = []

	for x in range(N) :
		row = [int(x) for x in input().split(' ')]
		COORDINATE.append(row)


	################################## input

	solution(COORDINATE, N, M)