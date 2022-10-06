#숨바꼭질 4
from collections import defaultdict, deque
    
N, K = map(int,input().split())

max_size = 100001
#수빈이가 특정 위치를 방문할 때 걸리는 시간(초)를 나타내는 정보
visited = [0] * max_size
#자식 노드가 부모 노드를 알기 위한 정보
check = [0] * max_size #수빈이가 동생을 만나기 전에 어떤 좌표 이동했는지 표시하는 정보

#동생이 있는 위치에 도달하는데까지 수빈이가 어떻게 이동을 했는가?
#최단 이동 어떻게 하는지 출력
def move(x):
  #경로 탐색 시작
  data = []
  #역으로 경로 찾기
  temp = x
  #수빈이가 동생을 만날 때까지의 걸리는 시간만큼 반복
  for _ in range(visited[x]+1):
    #현재 위치 추가
    data.append(temp)
    #전의 위치 받기
    temp = check[temp]
  print(' '.join(map(str,data[::-1])))
    
  
def bfs(start):
  q = deque()
  q.append(start)
  
  while q:
    x = q.popleft()
    if x == K:
      #동생을 만나는데 걸린 시간
      print(visited[x])
      #루트 출력
      move(x)
      return 
    #수빈이가 이동할 수 있는 3가지 방향(뒤, 앞, 순간이동)을 차례대로 받아
    for next in (x-1, x+1, x*2):
      #다음 이동할 위치가 이동가능한 좌표이며 아직 방문하지 않았다면
      if 0 <= next <= 100000 and visited[next] == 0:
        #이동할 위치에 시간 표시
        visited[next] = visited[x] + 1
        q.append(next)
        #수빈이가 지나온 위치를 알기위해 다음 이동 위치에 현재 이동위치 기록
        check[next] = x
        
bfs(N)