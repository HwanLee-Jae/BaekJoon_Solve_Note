def find_generator(n):
    # 1부터 n-1까지 반복하면서 생성자를 찾습니다.
    for i in range(1, n):
        # i와 i의 각 자리수의 합을 계산합니다.
        sum_digits = i + sum(map(int, str(i))) 
        
        # 계산된 합이 n과 같다면 i는 n의 생성자입니다.
        if sum_digits == n:
            return i  # 가장 작은 생성자인 i를 반환합니다.
    
    # n의 생성자가 없을 경우 0을 반환합니다.
    return 0

# 사용자로부터 정수 입력을 받습니다.
n = int(input())

# 입력된 정수 n에 대한 생성자를 찾고 출력합니다.
print(find_generator(n))
