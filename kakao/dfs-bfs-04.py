# https://www.welcomekakao.com/learn/courses/30/lessons/43164?language=python3
'''
dfs를 이용
dfs 함수를 짤 때, 어떤것들을 parameter로 받고 어떤 값을 return할 지를 잘 정해야함
'''


# route가 존재하면 route를 return, 존재하지 않으면 None을 return
def dfs(dic, routes, N):
    if len(routes) == N+1:
        return routes

    src = routes[-1]
    if src not in dic:
        return None

    dests = dic[src]
    for i in range(len(dests)):
        dest = dests.pop(i)
        result = dfs(dic, routes[:] + [dest], N)
        if result:
            return result

        else:
            dests.insert(i, dest)

    return None


def solution(tickets):
    dic = dict()
    for t in tickets:
        src, dest = t
        if src in dic:
            dic[src].append(dest)
        else:
            dic[src] = [dest]

    for src in dic:
        dic[src].sort()

    routes = ['ICN']
    return dfs(dic, routes, len(tickets))




# print(dfs([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']], 'ICN'))

# print(solution([['ICN', 'JFK']]))
# print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
# print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))
# print(solution([['ICN', 'K'], ['ICN', 'J'], ['K', 'ICN'], ['J', 'K']]))
print(solution([["ICN", "J"], ["ICN", "K"], ["K", "ICN"]]))
