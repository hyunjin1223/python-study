# problem: 1436
# tier: silver

# N번째 종말의 수를 찾기 위한 입력
n = int(input())

# 첫 번째 종말의 수인 666부터 시작
target = 666
count = 0

while True:
    # 숫자에 '666'이 포함되어 있는지 확인
    if '666' in str(target):
        count += 1
    
    # n번째 종말의 수를 찾았다면 출력하고 종료
    if count == n:
        print(target)
        break
    
    # 666이 포함된 수를 찾을 때까지 1씩 증가 (브루트 포스)
    target += 1