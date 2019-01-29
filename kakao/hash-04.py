# https://www.welcomekakao.com/learn/courses/30/lessons/42579?language=python3


def solution(genres, plays):
    dic = dict() # key: genre, value: array of (id, plays)
    arr = []
    answer = []

    # 장르별로 play 횟수를 모음
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in dic:
            dic[genre].append((i, play))

        else:
            dic[genre] = [(i, play)]

    for genre in dic:
        genre_musics = dic[genre]
        genre_sum = sum([x[1] for x in genre_musics])
        arr.append((genre, genre_sum))

    arr.sort(key=lambda x: -x[1]) # 장르별 총 재생횟수 합으로 정렬
    for (genre, plays) in arr:
        musics = dic[genre]
        musics.sort(key=lambda x: -x[1]) # 장르안에서 각 곡별 재생횟수로 정렬
        if len(musics) == 1:
            answer.append(musics[0][0])
        else:
            answer.append(musics[0][0])
            answer.append(musics[1][0])

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))