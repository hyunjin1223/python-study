# problem: 2941
# tier: silver

# 크로아티아 알파벳 변경 리스트
croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 단어 입력
word = input()

# 리스트에 있는 크로아티아 알파벳을 한 글자 기호('*')로 치환
for alpha in croatian_alphabets:
    word = word.replace(alpha, '*')

# 치환된 문자열의 길이를 출력
print(len(word))