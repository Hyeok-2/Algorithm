# 문제 : 천원을 내고 천원이하의 물건을 살 때 받을 거스름돈 동전의 개수가 최소가 되는 프로그램

price = int(input()) # 물건 가격 입력
money = [500, 100, 50, 10, 5, 1] # 거스름돈 동전의 종류
sum_count = 0 # 받을 동전의 개수의 합

rest_money = 1000 - price # 받을 거스름돈

# 동전 중 금액이 가장 큰 동전부터 최대로 나눠주기
for item in money:
    sum_count += rest_money // item
    rest_money %= item

print(sum_count)



