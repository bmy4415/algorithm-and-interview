# https://www.acmicpc.net/problem/14501 퇴사



def solution(n, arr) :
	answer = findMaxProfit(n, arr, 1, 0)
	print(answer)


def findMaxProfit(n, arr, curr_date, accumulated_profit) :
	if curr_date > n :
		return accumulated_profit

	time, profit = arr[curr_date]
	# 현재 날짜의 일 가능
	if curr_date + time <= n+1 :
		do = findMaxProfit(n, arr, curr_date+time, accumulated_profit+profit)		# 현재 날짜의 일을 하는 경우
		undo = findMaxProfit(n, arr, curr_date+1, accumulated_profit)				# 현재 날짜의 일을 하지 않는 경우
		return max(do, undo)

	else :
		return findMaxProfit(n, arr, curr_date+1, accumulated_profit)

if __name__ == '__main__' :
	N = int(input())
	ARR = [0] * (N+1)
	for i in range(1, N+1) :
		time, profit = [int(x) for x in input().split(' ')]
		ARR[i] = (time, profit)

	solution(N, ARR)