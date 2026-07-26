# problem: 13909
# tier: silver
import sys

# 창문 개수 입력
n = int(sys.stdin.readline())

# 약수의 개수가 홀수인 수만 마지막에 열려 있음
# 완전 제곱수만 약수의 개수가 홀수이므로
# n 이하의 완전 제곱수 개수를 구하면 됨

# 열린 창문 개수 출력
print(int(n**0.5))