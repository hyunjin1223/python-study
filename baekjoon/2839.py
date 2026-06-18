# problem: 2839
# tier: silver

# 배달해야 할 설탕 무게 N 입력
n = int(input())

# 봉지 개수를 세는 변수
bags = 0

while n >= 0:
    # 5로 나누어 떨어지는 경우, 가장 큰 봉지(5kg)로 모두 채우는 것이 최적
    if n % 5 == 0:
        bags += (n // 5)
        print(bags)
        break
    
    # 5로 나누어 떨어지지 않으면 3kg 봉지를 하나 쓰고 다시 확인
    n -= 3
    bags += 1
else:
    # n이 0보다 작아질 때까지 나누어 떨어지지 않으면 정확하게 만들 수 없는 무게
    print(-1)