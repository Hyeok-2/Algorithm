import sys

sys.setrecursionlimit(100000)

def dfs(n):
    visit[n] = True
    for i in graph[n]:
        if visit[i] == False:
            dfs(i)

n,m = map(int, input().split()) # 정점n개와 간선m개

graph = [[] for __ in range(n+1)]

for __ in range(m): # 노드끼리 입력한 간선의개수만큼 연결하기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (n+1)
output = 0
for i in range(1,n+1):
    if visit[i] == False:
        dfs(i)
        output += 1

print(output)



