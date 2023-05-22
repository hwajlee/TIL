import sys
sys.stdin = open('input.txt')

length = int(input())

for i in range(1, length+1):
    # 몇 개의 숫자를 받아올 것인가?
    t = input()
    # 받아올 숫자 리스트
    n = list(map(int, input().split()))

    max_num = min_num = n[0]
    for j in range(1, len(n)):
        # 탐색값이 최대값보다 크면 교체
        if n[j] > max_num :
            max_num = n[j]
        # 탐색값이 최소값보다 작으면 교체
        if n[j] < min_num:
            min_num = n[j]
    print("#{} {}".format(i, max_num - min_num))

