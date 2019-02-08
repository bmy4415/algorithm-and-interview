# https://www.welcomekakao.com/learn/courses/30/lessons/43162?language=python3
'''
0번부터 (n-1)번 컴퓨터까지, 각 컴퓨터마다 dfs 탐방을 통해 시작 컴퓨터의 번호를 전파하여 network list에 기록
특히 , i와 j가 이어져있으면 i에서 dfs 탐방 후 network[i] = network[j]가 되며, j에서 dfs 탐방을 진행하면
j에 연결된 것도 전부 i의 값으로 바뀜

network의 모든 node에 대해서 탐방을 진행한 후, network array에서 서로 다른 숫자의 갯수를 return하면 됨
'''


# start에서 시작하여 dfs 실행
# 중간중간에 network list에 기록
def dfs(network, start, computers):
    connected = computers[start]

    # 연결되어 있는 node가 하나도 없는 경우
    if not connected:
        return

    for node, link in enumerate(connected):
        # 자기 자신으로의 link
        if node == start:
            continue

        # 이미 같은 network인 경우
        if network[node] == network[start]:
            continue

        # start와 연결되어 있지만 같은 network가 아닌 경우 => 같은 network로 만들어줌
        if link and network[node] != network[start]:
            network[node] = network[start]
            dfs(network, node, computers)

    return


def solution(n, computers):
    network = list(range(n))
    for i in network:
        dfs(network, i, computers)

    return len(set(network))


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2
# solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) # 1