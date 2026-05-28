# problem: 2745
# tier: bronze

# 진법 수 N과 진법 B 입력
N, B = input().split()
B = int(B)

# int(문자열, 진법) 함수를 사용하면 
# B진법 수 N을 10진법으로 간단히 변환할 수 있음
print(int(N, B))