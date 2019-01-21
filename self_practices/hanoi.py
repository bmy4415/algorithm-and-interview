# 하노이의 탑 문제

def hanoi(n, start, middle, end) :
    if n == 1:
        print('1: {} -> {}'.format(start, end))
        return

    hanoi(n-1, start, end, middle)
    print('{}: {} -> {}'.format(n, start, end))
    hanoi(n-1, middle, start, end)

hanoi(3, 1,2,3)