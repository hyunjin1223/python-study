# problem: 11718
# tier: bronze

# 입력이 더 이상 없을 때까지 그대로 출력 (EOF 처리)
while True:
    try:
        # 한 줄씩 입력받기
        line = input()
        # 입력받은 그대로 출력
        print(line)
    except EOFError:
        # 입력이 끝나면 반복문 종료
        break