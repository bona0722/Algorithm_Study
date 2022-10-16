#BOJ17086_아기상어2
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()

def bfs():
  global graph, q, N, M
  dys, dxs = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
  while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      #이동한 칸이 0이면 이동 거리 저장
      if graph[nx][ny] == 0:
        q.append([nx,ny])
        graph[nx][ny] = graph[x][y] + 1
        
  return

#상어 위치 큐에 삽입
for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      q.append([i,j])
        
bfs()

#저장된 최대값을 찾은 뒤 1을 빼고 출력
dist = -1
for i in range(N):
  for j in range(M):
    dist = max(dist, graph[i][j])
    
print(dist - 1)

'''

안전 거리 = 그 칸과 가장 거리가 가까운 아기 상어와의 거리
두 칸의 거리 = 하나의 칸에서 다른 칸으로 가기 위해 지나야 하는 칸의 수
이동은 인접한 8방향으로 가능


visited 만들어서 하니까 반복이 심해짐. graph에 바로 저장
'''