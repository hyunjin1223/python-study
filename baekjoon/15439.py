# problem: 15439
# tier: bronze
import sys

# 베라가 가진 옷의 색상 수 N 입력
n = int(sys.stdin.readline())

# 상의와 하의의 색상이 서로 달라야 함
# 상의를 고르는 경우의 수: N
# 하의를 고르는 경우의 수: 상의와 같은 색을 제외한 (N - 1)
# 따라서 전체 경우의 수는 N * (N - 1)
print(n * (n - 1))