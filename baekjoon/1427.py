# problem: 1427
# tier: silver

# 정수 N을 입력받음
n = input()

# 숫자의 각 자릿수를 리스트의 요소로 변환
# 예: "2143" -> ['2', '1', '4', '3']
digits = list(n)

# 자릿수를 내림차순(큰 수부터)으로 정렬
digits.sort(reverse=True)

# 리스트의 요소들을 하나의 문자열로 합쳐서 출력
print(''.join(digits))