import sys

sys.setrecursionlimit(100000)  # 파이썬은 기본 재귀 깊이가 1000이므로 더 늘려줬음 --> 백준 런타임오류 해결!!


def isTrue(x,y):
    if x > -1 and x < n and y >-1 and y<m:
        return True

def dfs(x,y):

    global cnt

    if  isTrue(x,y) and nemo[x][y] == 0:
        nemo[x][y] = 1
        cnt += 1
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            dfs(nx,ny)

        return True
    
    else:
        return False


m,n,k = map(int,input().split()) # 열 m x 행 n 사각형 만들고 k개의 직사각형 좌표

#사각형 내부 색칠 안된 것 0으로 초기화
nemo = [ [] for __ in range(n)]
for x in range(n):
    for __ in range(m):
        nemo[x].append(0)

# 입력한 좌표들 색칠하기 (1로 표시)
for __ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            nemo[x][y] = 1

empty_area = [] # 비어있는 영역들의 각 넓이

cnt = 0 # 비어있는 영역의 넓이 즉, 넓이가 1이므로 개수임

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

# 각좌표별로 dfs탐색
for x in range(n):
    for y in range(m):        
        if dfs(x,y) == True:
            empty_area.append(cnt)
            cnt = 0

empty_area.sort() # 오름차순 정렬

print(len(empty_area))
for n in empty_area:
    print(n, end=" ")


   
    

