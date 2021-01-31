n, k = map(int, input().split()) # 동전의 종류 개수N  만들 값 K

coin_types = [] # 동전의 종류 리스트
# 동전 종류 입력하기
for __ in range(n):
    coin_type = int(input())
    coin_types.append(coin_type)

# 동전 종류 내림차순 정렬
coin_types.sort()
coin_types.reverse()

# k값을 만들기위한 동전의 최소개수 연산
coin_count = 0
for coin in coin_types:
    coin_count += k // coin
    k %= coin

print(coin_count)
