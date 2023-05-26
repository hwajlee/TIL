import sys
sys.stdin = open('input.txt')
# 오답 ..
# 테스트 케이스 수
T = int(input())

# 10X10 격자 생성
map_lst = [[0 for _ in range(10)] for _ in range(10)]
#print(map_lst[1][2:4])
#map_lst[1][2] = 1

cnt_lst = []
for TC in range(1, T+1):
    N = int(input())

    for i in range(0, N):
        # 행렬 좌표 값 및 color 받아오기 
        # 1 - red, 2 - blue 
        idx_color = list(map(int, input().split()))
        r1 = idx_color[0]
        c1 = idx_color[1]
        r2 = idx_color[2]
        c2 = idx_color[3]
        color = idx_color[4]

        cnt = 0
        for j in range(0, (r2-r1)+1):
            for r in range(0, (c2-c1)+1):
                if map_lst[r1+j][c1+r] == 0:
                    map_lst[r1+j][c1+r] = color
                elif map_lst[r1+j][c1+r] != 3 and map_lst[r1+j][c1+r]:
                    map_lst[r1 + j][c1 + r] = 3
                    cnt += 1

    map_lst = [[0 for _ in range(10)] for _ in range(10)]
    print(f'#{TC} {cnt}')
