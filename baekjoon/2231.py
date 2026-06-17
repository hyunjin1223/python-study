# problem: 2231
# tier: bronze

N = int(input())
result = 0

# 1부터 N까지 순회하며 생성자 찾기
for i in range(1, N + 1):
    # i와 i의 각 자릿수 합 계산 (분해합)
    sum_digits = i + sum(map(int, str(i)))
    
    # 분해합이 N과 같다면 i는 N의 생성자
    if sum_digits == N:
        result = i
        break

# 생성자를 찾으면 출력, 못 찾으면 0 출력
print(result)