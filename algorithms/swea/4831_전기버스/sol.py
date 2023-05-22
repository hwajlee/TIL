import sys
sys.stdin = open('input.txt')

# 테스트 케이스 수 입력
T = int(input())

# T만큼 테스트 케이스 반복
for TC in range(1, T+1):
    K, N, M = list(map(int, input().split()))

    # 충전기가 설치된 정류장 번호 리스트
    charge_station = list(map(int, input().split()))
    # 충전횟수 및 현재 위치
    charge_cnt = current = 0

    # 종점에 도착할 때까지 반복
    # 현재 위치에서 한번 충전으로 이동 가능한 정류소 K를 더한 결과가 종점인 N보다 작다면 while문 반복
    while current + K < N:
        for step in range(K, 0, -1):
            # 현재 위치 + 이동 거리만큼 이동했을 때 충전기가 있는 정류장일 경우
            if (current + step) in charge_station:
                # 현재 위치를 변경
                current += step
                # 충전횟수 +1
                charge_cnt += 1
                # for문 종료
                break
        # 충전기 설치가 잘못되었을 경우 while문 종료
        else:
            charge_cnt = 0
            break
    print("#{} {}".format(TC, charge_cnt))
