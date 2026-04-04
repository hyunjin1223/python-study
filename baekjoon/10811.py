# problem: 10811
# tier: bronze

# 바구니 개수 N과 순서 변경 횟수 M 입력
N, M = map(int, input().split())

# 1부터 N까지 번호가 매겨진 바구니 생성
arr = list(range(1, N + 1))

# M번 동안 지정된 범위(i~j)의 바구니 순서를 뒤집음
for _ in range(M):
    i, j = map(int, input().split())
    # 슬라이싱을 이용해 해당 구간을 역순으로 변경
    arr[i-1:j] = arr[i-1:j][::-1]

# 최종 바구니 상태 출력
print(*arr)