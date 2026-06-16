# problem: 1620
# tier: silver
import sys

# 입력 데이터와 쿼리가 각각 100,000개로 매우 많으므로 sys.stdin.readline 필수
input = sys.stdin.readline

n, m = map(int, input().split())

# 번호로 이름을 찾을 때는 리스트(인덱스)가 유리하고,
# 이름으로 번호를 찾을 때는 딕셔너리(해시)가 유리함
# 따라서 두 가지 자료구조를 모두 준비
num_to_name = {}
name_to_num = {}

for i in range(1, n + 1):
    name = input().strip()
    num_to_name[i] = name
    name_to_num[name] = i

for _ in range(m):
    query = input().strip()
    
    # 입력받은 쿼리가 숫자인지 문자인지 판별
    if query.isdigit():
        # 숫자라면 번호에 맞는 포켓몬 이름 출력
        print(num_to_name[int(query)])
    else:
        # 문자라면 이름에 맞는 번호 출력
        print(name_to_num[query])