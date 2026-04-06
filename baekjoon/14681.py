# problem: 14681
# tier: bronze

# x, y 좌표 입력
x = int(input())
y = int(input())

# 사분면 판별 및 출력
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x > 0 and y < 0:
    print(4)
else:
    print(3)