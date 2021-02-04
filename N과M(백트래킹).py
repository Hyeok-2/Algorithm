def dfs(num):
    
    for nn in num_list[num]:
        if visit[nn] == 0:
            visit[nn] = 1
            seq.append(nn)
            dfs(nn)
            if len(seq) == m: # 수열 m개를 만족하면 출력
                for node in seq:
                    print(node, end=" ")
                print()
            visit[nn] = 0
            seq.remove(nn)
            
n,m = map(int, input().split()) # 1~n까지 숫자로 만들 수 있는 m개의 모든 수열
visit = [0] * (n+1) # n+1개  방문하지않은 배열 만들기 
num_list = [[] for __ in range(n+1)] # 각 요소 별로 본인을 제외한 나머지 숫자 기입

for i in range(1,n+1):
     for x in range(1,n+1):
         if i != x:
             num_list[i].append(x)

# 수열의 개수가 1일때는 1~n까지 순서대로 출력
if m == 1:
    for item in range(1,n+1):
        print(item)
# 수열개수가 2이상일때는 백트래킹 dfs 함수 호출
else:
    seq = []
    for a in range(1,n+1):
        seq.append(a)
        visit[a] = True
        dfs(a)
        visit[a] = False
        seq.clear()


             