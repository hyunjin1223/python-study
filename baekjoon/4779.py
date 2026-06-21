# problem: 4779
# tier: silver
import sys

# 칸토어 집합: 선분을 3등분하여 가운데 부분을 반복적으로 제거하는 과정
# N이 주어졌을 때, 3^N 길이의 선분에 대해 이 과정을 수행한 최종 형태 출력
# 입력이 더 이상 없을 때까지 수행해야 하므로 sys.stdin.read() 사용

def cantor(n):
    # 기본 케이스: N이 0이면 선분의 길이는 3^0 = 1, '-' 하나 출력
    if n == 0:
        return "-"
    
    # 이전 단계(n-1)의 결과를 가져옴
    prev = cantor(n - 1)
    
    # 칸토어 집합의 규칙: (이전 단계) + (이전 단계 길이만큼의 공백) + (이전 단계)
    # 3등분 중 왼쪽과 오른쪽은 유지하고 가운데만 공백으로 치환하는 것과 같음
    return prev + " " * (3**(n - 1)) + prev

# 파일 끝(EOF)까지 입력을 읽어 들임
lines = sys.stdin.read().splitlines()

for line in lines:
    n = int(line)
    print(cantor(n))