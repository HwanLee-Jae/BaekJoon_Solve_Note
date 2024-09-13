# 입력받기
n, m = map(int, input().split())  # 보드의 행(N)과 열(M) 크기를 입력받습니다.

# 보드의 각 행을 입력받아 리스트로 저장
board = [input().strip() for _ in range(n)]  # 보드의 각 행을 문자열로 입력받습니다.

# 결과를 저장할 리스트 초기화
result = []

# 보드에서 8x8 크기의 모든 가능한 부분 보드를 검사
for i in range(n - 7):  # 시작 행을 0부터 n-8까지 반복합니다.
    for j in range(m - 7):  # 시작 열을 0부터 m-8까지 반복합니다.
        cnt1 = 0  # 첫 번째 패턴의 변경 횟수를 세기 위한 변수
        cnt2 = 0  # 두 번째 패턴의 변경 횟수를 세기 위한 변수
        
        # 현재 8x8 부분 보드에서 색상 패턴 비교
        for a in range(i, i + 8):  # 부분 보드의 행을 반복합니다.
            for b in range(j, j + 8):  # 부분 보드의 열을 반복합니다.
                # (a+b) % 2에 따라 패턴을 결정합니다.
                if (a + b) % 2 == 0:  # (a+b)가 짝수인 경우
                    # 패턴1: (a+b) % 2가 짝수일 때 'B', 홀수일 때 'W'
                    if board[a][b] != 'B':
                        cnt1 += 1  # 패턴1과 다른 경우 변경 횟수 증가
                    if board[a][b] != 'W':
                        cnt2 += 1  # 패턴2와 다른 경우 변경 횟수 증가
                else:  # (a+b)가 홀수인 경우
                    # 패턴1: (a+b) % 2가 홀수일 때 'W', 짝수일 때 'B'
                    if board[a][b] != 'W':
                        cnt1 += 1  # 패턴1과 다른 경우 변경 횟수 증가
                    if board[a][b] != 'B':
                        cnt2 += 1  # 패턴2와 다른 경우 변경 횟수 증가
        
        # 두 패턴에 대한 변경 횟수를 결과 리스트에 추가
        result.append(cnt1)
        result.append(cnt2)
        
# 모든 8x8 부분 보드에서의 최소 변경 횟수를 출력
print(min(result))
