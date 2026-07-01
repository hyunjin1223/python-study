# problem: 2447
# tier: gold
import sys

# 별 찍기 - 10: 재귀적인 패턴을 활용하여 별을 찍는 문제
# N이 3의 거듭제곱(3, 9, 27, ...)일 때, 공백으로 비워진 가운데를 제외한 패턴 반복

def draw_stars(n):
    # 기본 케이스: n이 1이면 별 하나 반환
    if n == 1:
        return ["*"]

    # n/3 크기의 패턴을 먼저 구함
    stars = draw_stars(n // 3)
    result = []

    # 1. 상단 1/3 (패턴 3개 나열)
    for s in stars:
        result.append(s * 3)
        
    # 2. 중단 1/3 (패턴 + 공백 + 패턴)
    for s in stars:
        result.append(s + " " * (n // 3) + s)
        
    # 3. 하단 1/3 (패턴 3개 나열)
    for s in stars:
        result.append(s * 3)

    return result

# N 입력
n = int(sys.stdin.readline())

# 함수 호출 및 리스트 요소를 한 줄씩 출력
print('\n'.join(draw_stars(n)))