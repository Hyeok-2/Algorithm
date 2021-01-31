from collections import deque

# 촌수계산
def bfs(a, b, a_chonsoo):  #  a와 b의 촌수관계
    queue = deque()
    queue.append(a)
    while True:
        v = queue.popleft()
        for i in chonsoo[v]:
            if visited[i] == False:
                a_chonsoo[i] = a_chonsoo[v] + 1
                queue.append(i)
                visited[i] = True
        
        if visited[b] == True:
            return a_chonsoo[b]
        if len(queue) == 0:
            return -1
            

n = int(input()) # 사람수 입력
n1, n2 = map(int, input().split()) # 두 사람사이의 촌수 관계
m = int(input()) # 부모자식 관계를 나타낼 개수

chonsoo = [[] for __ in range(n+1)] # 각 사람별로 1촌관계를 나타낼 리스트

# m의 개수만큼 입력한 1촌관계 그래프 만들기
for __ in range(m):
    a, b = map(int, input().split())
    chonsoo[a].append(b)
    chonsoo[b].append(a)

# 촌수관계를 파악할 사람 한명(n1)을 제외한 나머지사람한테 방문x 초기화
visited = [False for __ in range(n+1)]
visited[n1] = True 

# n1의 촌수 관계
n1_chonsoo = [0 for __ in range(n+1)]
for i in chonsoo[n1]:
    n1_chonsoo[i] += 1

print(bfs(n1,n2,n1_chonsoo))

