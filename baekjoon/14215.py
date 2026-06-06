# problem: 14215
# tier: bronze

# 세 변의 길이를 리스트로 입력받아 정렬
sides = sorted(list(map(int, input().split())))

# 삼각형 성립 조건: a + b > c (가장 긴 변이 나머지 두 변의 합보다 작아야 함)
# 조건을 만족하지 못하면 가장 긴 변(sides[2])을 (sides[0] + sides[1] - 1)로 조정
if sides[0] + sides[1] <= sides[2]:
    sides[2] = sides[0] + sides[1] - 1

# 만들 수 있는 가장 큰 둘레 출력
print(sum(sides))