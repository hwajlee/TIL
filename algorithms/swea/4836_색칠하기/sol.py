import sys

sys.stdin = open('input.txt')

# 테스트 케이스 수 받아 오기
T = int(input())

# 테스트 케이스 수 만큼 반복
for TC in range(1, T+1):
    N = int(input())
    # 10X10 격자 생성
    map_lst = [[0 for _ in range(10)] for _ in range(10)]

    for n in range(0, N):
        # r1, c1, r2, c2, color 받아 오기
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if map_lst[r][c] == 0:
                    map_lst[r][c] = color
                else:
                    map_lst[r][c] += color
    cnt = 0
    for x in range(len(map_lst)):
        for y in range(len(map_lst[x])):
            if map_lst[x][y] == 3:
                cnt += 1
    print(f'#{TC} {cnt}')

