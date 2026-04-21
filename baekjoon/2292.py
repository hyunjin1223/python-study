# problem: 2292
# tier: bronze

n = int(input())

num = 1 # 벌집의 최대 숫자
cnt = 1 # 지나는 방의 개수 (층수)

# 입력값이 현재 층의 최대 숫자보다 크면 다음 층으로 이동
while n > num:
    num += 6 * cnt # 6의 배수만큼 방이 늘어남
    cnt += 1

print(cnt)