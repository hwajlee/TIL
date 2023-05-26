import sys
import math
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())

    # N(열) X M(행) 격자 생성
    str_lst = [[0 for _ in range(N)] for _ in range(M)]

    # M만큼 행이 만들어져야 함
    for m in range(0, M):
        input_lst = list(map(str, input()))
        for n in range(0, N):
            str_lst[m][n] = input_lst[n]

    N2 = math.floor(N/2)
    M2 = math.floor(M/2)
    row_cnt = 0
    col_cnt = 0
    result_lst = []

    # N(열) = 20, M(행) = 13이라면..
    for m in range(0, M):
        for n in range(0, N2):
            # 행 체크 (행 고정 후 컬럼만 변화)
            if str_lst[m][n] == str_lst[m][N2-n-1]:
                row_cnt += 1
                if row_cnt == N2:
                    result_lst.append(str_lst[m])
                    row_cnt = 0
            else:
                break

    for n in range(0, N):
        for m in range(0, M2):
            # 열 체크 (열 고정 후 행만 변화)
            if str_lst[m][n] == str_lst[M2-m-1][n]:
                col_cnt += 1
                if col_cnt == M2:
                    result_lst.append(str_lst[:][n])
                    col_cnt = 0
                else:
                    break
    print(result_lst)
