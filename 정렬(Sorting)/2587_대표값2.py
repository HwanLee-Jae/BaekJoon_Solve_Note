#문제
#어떤 수들이 있을 때, 그 수들을 대표하는 값으로 가장 흔하게 쓰이는 것은 평균이다. 평균은 주어진 모든 수의 합을 수의 개수로 나눈 것이다. 예를 들어 10, 40, 30, 60, 30의 평균은 (10 + 40 + 30 + 60 + 30) / 5 = 170 / 5 = 34가 된다.

#평균 이외의 또 다른 대표값으로 중앙값이라는 것이 있다. 중앙값은 주어진 수를 크기 순서대로 늘어 놓았을 때 가장 중앙에 놓인 값이다. 예를 들어 10, 40, 30, 60, 30의 경우, 크기 순서대로 늘어 놓으면

#10 30 30 40 60

#이 되고 따라서 중앙값은 30이 된다.

#다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

#입력
#첫째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 주어지는 자연수는 100 보다 작은 10의 배수이다.

#출력
#첫째 줄에는 평균을 출력하고, 둘째 줄에는 중앙값을 출력한다. 평균과 중앙값은 모두 자연수이다.

#에시 입력
#10
#40
#30
#60
#30

#예제 출력
#34
#30

# 빈 리스트 arr를 생성합니다. 이 리스트에 입력된 숫자를 저장할 것입니다.
arr = []

# 5개의 숫자를 입력받아 리스트에 추가하는 반복문입니다.
for i in range(5):
    # 각 입력값을 정수형으로 변환하여 리스트에 추가합니다.
    arr.append(int(input()))  # 사용자로부터 숫자를 입력받아 arr 리스트에 추가

# 리스트에 저장된 숫자들을 오름차순으로 정렬합니다.
arr.sort()

# 평균 계산: 리스트의 모든 숫자의 합을 구한 뒤 5로 나누어 평균을 구합니다.
avg = sum(arr) / 5  # sum() 함수는 리스트에 있는 모든 요소의 합을 반환

# 평균값을 출력하는데, 소수점을 버리기 위해 int() 함수로 정수형으로 변환하여 출력합니다.
print(int(avg))

# 중앙값 출력: 오름차순으로 정렬된 리스트의 가운데 값(세 번째 값)을 출력합니다.
# 리스트의 인덱스는 0부터 시작하므로, 5개의 요소 중에서 가운데 값은 인덱스 2에 해당합니다.
print(arr[2])
