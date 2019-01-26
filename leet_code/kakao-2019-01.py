# https://www.welcomekakao.com/learn/courses/30/lessons/42888?language=python3
'''
record example
- Enter [user id] [nick name]
- Leave [user id]
- Change [user id] [nick name]
[user id]로 user 구분
- record를 parsing하면서 command가 Enter/Leave면 [user id] [command] 형태로 저장
- record를 parsing하면서 command가 Change면 uid_nickname_dict에서 변경
- 맨 마지막에 user id에 해당하는 nick name을 찾아서 메시지로 변경

map 보다 list 순회가 더 빠른 것 같음(27번 test case, map:145ms, list iteration:134ms)
'''


def solution(record):
    answer = []
    uid_nickname_dict = dict()
    # record parsing
    for r in record:
        command, *arg = r.split(' ')

        if command == 'Enter':
            user_id, nickname = arg
            answer.append([user_id, command])
            uid_nickname_dict[user_id] = nickname

        elif command == 'Leave':
            user_id = arg[0]
            answer.append([user_id, command])

        elif command == 'Change':
            user_id, nickname = arg
            uid_nickname_dict[user_id] = nickname

    # # message 작성
    # def message(arg):
    #     user_id, command = arg
    #     if command == 'Enter':
    #         return uid_nickname_dict[user_id] + '님이 들어왔습니다.'
    #     elif command == 'Leave':
    #         return uid_nickname_dict[user_id] + '님이 나갔습니다.'

    for idx, a in enumerate(answer):
        user_id, command = a
        if command == 'Enter':
            answer[idx] = uid_nickname_dict[user_id] + '님이 들어왔습니다.'
        elif command == 'Leave':
            answer[idx] = uid_nickname_dict[user_id] + '님이 나갔습니다.'

    # return list(map(message, answer))
    return answer


result = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
for r in result:
    print(r)