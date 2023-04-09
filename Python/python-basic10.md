# 추상자료형 (Abstract Data Type)
stack, queue, graph

# Stack
LIFO
1. push
2. pop

# Queue
FIFO
1. engue
2. degue

# Graph
cycle이 있음
1. 방향 그래프
2. 무방향 그래프
3. 가중치 그래프

## Tree
cycle이 없음
1. 깊이 우선 탐색 (DFS) : 목적이 있을 때
2. 넓이 우선 탐색 (BFS) : 최단


# Graph by 2d array (이차원배열)
정점과 정점의 관계를 찾을 때 빠름

Vertax 낮고, Edge 높으면 => 이차원배열이 유리
O(1)

# Graph by Adj List (인접리스트)
Vertax 높고, Edge 낮으면 => 인접리스트가 유리

순회(반복)
O(n)

|Graph by Adj List|Graph by 2d array|
|-|-|
|공간복잡도 안좋음|공간복잡도 좋음|
|시간복잡도 좋음|시간복잡도 안좋음|


