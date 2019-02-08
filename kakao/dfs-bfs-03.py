# https://www.welcomekakao.com/learn/courses/30/lessons/43163?language=python3
'''

'''



# 두 단어 사이의 다른 알파벳 갯수를 구함
def diff(src, dest):
    count = 0
    for i in range(len(src)):
        if src[i] != dest[i]:
            count +=1

    return count


def solution(begin, target, words):
    if not words:
        return 0

    candidates = []

    for i, word in enumerate(words):
        if diff(begin, word) != 1:
            continue

        if word == target:
            return 1

        temp = words[:i] + words[i+1:]
        if solution(word, target, temp) != 0:
            candidates.append(1 + solution(word, target, temp))

    if not candidates:
        return 0

    return min(candidates)


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
