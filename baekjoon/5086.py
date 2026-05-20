# problem: 5086
# tier: bronze

while True:
    a, b = map(int, input().split())
    
    # 0 0 입력 시 종료
    if a == 0 and b == 0:
        break
    
    # 약수 관계 확인
    if b % a == 0:
        print("factor")
    # 배수 관계 확인
    elif a % b == 0:
        print("multiple")
    # 둘 다 아닌 경우
    else:
        print("neither")