from itertools import combinations  # itertools 모듈에서 combinations 함수 불러오기 (조합을 구하기 위해 사용)

# 입력 받기
n, m = map(int, input().split())  # n: 카드의 개수, m: 목표 합. 첫 줄에서 n과 m을 입력받아 각각 정수로 변환
cards = list(map(int, input().split()))  # 두 번째 줄에서 각 카드에 적힌 수들을 입력받아 리스트로 저장

# 최대 합을 저장할 변수를 초기화
max_sum = 0  # 목표 합 m을 넘지 않으면서 가장 큰 세 카드의 합을 저장할 변수. 초기값은 0으로 설정

# 카드 중 3장을 뽑는 모든 조합을 구하기
# combinations(cards, 3)은 cards 리스트에서 3개의 요소를 선택하는 모든 조합을 반환함
for combination in combinations(cards, 3):  
    current_sum = sum(combination)  # 선택된 3장의 카드의 합을 계산하여 current_sum에 저장
    
    # 만약 이 세 카드의 합이 목표 값 m을 넘지 않는다면
    if current_sum <= m:
        # 현재까지 찾은 합 중에서 가장 큰 값을 저장
        # max 함수는 두 값을 비교하여 더 큰 값을 반환함. 기존의 max_sum과 현재 계산한 current_sum 중 더 큰 값을 max_sum에 저장
        max_sum = max(max_sum, current_sum)

# 최종적으로 m을 넘지 않으면서 가장 큰 세 카드의 합을 출력
print(max_sum)  # 결과 출력

