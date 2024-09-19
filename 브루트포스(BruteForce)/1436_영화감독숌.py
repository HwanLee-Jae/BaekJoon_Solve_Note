# 사용자로부터 n을 입력받습니다. n은 찾고자 하는 '666'이 포함된 숫자의 순서를 의미합니다.
n = int(input())

# 카운터 변수인 cnt는 '666'이 포함된 숫자를 찾을 때마다 증가시키는 용도입니다.
cnt = 0

# result는 '666'이 포함된 숫자를 찾기 위한 시작 숫자입니다. 가장 작은 '666'을 포함한 숫자는 666이므로 처음 값을 666으로 설정합니다.
result = 666

# 무한 반복을 사용하여 조건을 만족하는 '666'이 포함된 숫자를 찾습니다.
while True:
    # result를 문자열로 변환한 후 '666'이 포함되어 있는지 확인합니다.
    # 만약 '666'이 문자열 내에 있다면 조건을 만족하는 숫자입니다.
    if '666' in str(result):
        # 조건을 만족하는 경우 카운터를 증가시킵니다.
        cnt += 1
    
    # 카운터 cnt가 n과 같아졌을 때, n번째로 '666'이 포함된 숫자를 찾은 것이므로 반복문을 종료합니다.
    if cnt == n:
        break
    
    # '666'을 포함하는 다음 숫자를 찾기 위해 result를 1씩 증가시킵니다.
    result += 1

# 반복문이 끝나면 n번째로 '666'이 포함된 숫자가 result에 저장되므로 해당 숫자를 출력합니다.
print(result)
