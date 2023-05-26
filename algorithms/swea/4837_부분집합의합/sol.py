import sys
sys.stdin = open('input.txt')

T = int(input())

# 참고) 원소 개수가 n인 집합 s의 전체 부분집합의 개수는 2**n

for TC in range(1, T+1):
    # N: 부분 집합 원소의 개수
    # K: 부분 집합 원소의 총 합
    N, K = map(int, input().split())

    # 1~12까지 숫자를 원소로 가진 집합
    arr = [_ for _ in range(1, 13)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # 부분 집합 원소의 개수가 N이고 합이 K인 부분집합의 개수
    result = 0

    # 모든 부분 집합 확인
    for i in range(1<<12):
        # 부분 집합의 합
        subset_sum = 0
        # 부분집합
        subset = []
        for j in range(12):
            if i & (1<<j):
                # j번째 요소는 부분집합에 포함
                subset_sum += arr[j]
                subset.append(arr[j])
        # 부분 집합의 원소의 개수가 N, 부분 집합 원소의 총 합이 K인 부분집합 개수
        if len(subset) == N and subset_sum == K:
            result += 1
        print(f'#{TC} {result}')

# & 연산자
# i & (1<<j): i의 j번째 비트가 1인지 아닌 지를 검사함
# (1<<j)는 j번째 비트만 1

if i & (1<<j):
    print('i의 j번째 비트가 1')
else:
    print('i의 j번째 비트가 0')

# i가 5라면, 101(2)이므로
# 1<<0: True
# 1<<1: False
# 1<<2: True