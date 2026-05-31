# problem: 2869
# tier: bronze
import math

# 낮(A), 밤(B), 목표(V) 입력
A, B, V = map(int, input().split())

# 마지막 날 낮에 정상에 도달하면 미끄러지지 않음
# (목표 - 밤) / (낮 - 밤) 을 통해 소요 일수 계산
days = (V - B) / (A - B)

# 소수점 발생 시 하루가 더 필요하므로 올림 처리
print(math.ceil(days))