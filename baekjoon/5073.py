# problem: 5073
# tier: bronze

while True:
    # 세 변의 길이 입력 및 정렬
    sides = sorted(list(map(int, input().split())))
    
    # 0 0 0 입력 시 종료
    if sum(sides) == 0:
        break
    
    # 삼각형 성립 조건: 가장 긴 변의 길이가 나머지 두 변의 합보다 작아야 함
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    # 세 변의 길이가 모두 같은 경우
    elif sides[0] == sides[1] == sides[2]:
        print("Equilateral")
    # 두 변의 길이만 같은 경우
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        print("Isosceles")
    # 세 변의 길이가 모두 다른 경우
    else:
        print("Scalene")