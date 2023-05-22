import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    # 정수의 개수 N과 구간의 개수 M
    N, M = list(map(int, input().split()))

    number = list(map(int, input().split()))
    sum_list = []

    for l in range(0, N-M+1):
        sum_list.append(sum(number[l:l+M]))
    print(f'#{TC} {max(sum_list) - min(sum_list)}')


# 방법 2
T = int(input())

for SN in range(1, T + 1):
    N = list(map(int, input().split()))
    n_count = N[0]
    scope = N[1]
    numbers = list(map(int, input().split()))
    sum_max = sum_min = numbers[0]

    for i in range(0, n_count - scope + 1):
        j = i + scope
        sum_numbers = sum(numbers[i:j])
        if sum_numbers > sum_max:
            sum_max = sum_numbers
        elif sum_numbers < sum_min:
            sum_min = sum_numbers

    ans = sum_max - sum_min

    print(f'#{SN} {ans}')