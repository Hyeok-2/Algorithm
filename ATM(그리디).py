n = map(int, input().split()) # 사람수
times = list(map(int, input().split())) # 각 사람들이 인출하는데 걸리는 시간

people_sum = 0 # 모든 사람들이 인출하는데 걸린 최소시간
time = 0 # n번째 사람이 인출하는데 걸리는 시간

# 총 걸린시간이 최소가되는 연산
while len(times) != 0:
    time += min(times)
    people_sum += time
    times.remove(min(times))

# 총 걸린시간 출력(최소값)
print(people_sum)
