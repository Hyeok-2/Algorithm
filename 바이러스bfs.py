from collections import deque

def bfs(n):
    queue = deque()
    queue.append(n)
    while len(queue) != 0:
        v = queue.popleft()
        for i in com_net[v]:
            if visit[i] == False:
                visit[i] = True
                queue.append(i)


n = int(input()) # 총 컴퓨터 개수
net_num = int(input()) # 네트워크 연결 개수

com_net = [[] for __ in range(n+1)] # 네트워크 연결 컴퓨터 목록

for __ in range(net_num):
    a,b = map(int,input().split())
    com_net[a].append(b)
    com_net[b].append(a)

visit = [False] * (n+1)
visit[1] = True


bfs(1)
print(visit.count(True)-1)