# https://www.welcomekakao.com/learn/courses/30/lessons/42577?language=python3


def solution(phone_book):
    dic = dict()
    phone_book.sort()

    for number in phone_book:
        for i in range(1, len(number)+1):
            prefix = number[0:i]

            if prefix in dic:
                return False

        dic[number] = True

    return True


print(solution(['119', '97674223', '1195524421'])) # false
print(solution(['123','456','789'])) # true
print(solution(['12','123','1235','567','88']	)) # false