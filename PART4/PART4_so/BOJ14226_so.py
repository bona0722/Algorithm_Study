#BOJ14226_이모티콘
from collections import deque

def bfs():
  global S, visited
  q = deque()
  q.append([1, 0]) #screen에 있는 이모티콘 개수, 클립보드에 복사된 이모티콘 개수
  visited[1][0] = 0
  
  while q:
    s, c = q.popleft()
    
    if s == S: return visited[s][c]
    #화면에 있는 이모티콘을 복사해서 클립보드에 저장한다. 이 때 덮어쓰기를 함
    if visited[s][s] == -1:
      visited[s][s] = visited[s][c] + 1
      q.append([s, s])
    
    #클립보드가 차 있을 때 화면에 클립보드의 모든 이모티콘을 붙여넣기 한다 
    if s + c <= S and visited[s+c][c] == -1:
      visited[s+c][c] = visited[s][c] + 1
      q.append([s+c,c])

    #화면에 있는 이모티콘 중 하나를 삭제한다.
    if s - 1 >= 0 and visited[s-1][c] == -1:
      visited[s-1][c] = visited[s][c] + 1
      q.append([s-1,c]) 
      
S = int(input())
visited = [[-1] * (S+1) for _ in range(S+1)]
print(bfs())  
# print(visited[])  

  
  
'''
이모티콘 S개 만드는 법
1. 화면에 있는 이모티콘 모두 복사해서 클립보드에 저장(이모티콘 복사할 때 이전 클립보드에 있던 내용은 덮어쓰기 됨)
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 함 (단, 비어있을 땐 불가능)
3. 화면에 있는 이모티콘 중 하나를 삭제(클립보드에 있는 이모티콘 일부 삭제 불가능)

화면에 이모티콘 붙여넣기 시, 클립보드에 있는 이모티콘의 개수가 화면에 출력

총 1초 

S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최소값 - BFS


[조건]

조건 1 클립보드에 이모티콘 복사하면 이전에 있던 내용은 덮어쓰기가 됨
조건 2 클립보드가 비어 있으면 붙여넣기 불가능
조건 3 클립보드에 있는 이모티콘의 개수가 화면에 몽땅 추가됨
q에 화면에 있는 이모티콘 개수, 클립보드 내 이모티콘 개수, cnt를 다 집어넣음


q에 screen에 들어있는 개수와 최솟값을 같이 저장해보기



실패 1
#1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
def copy_screen(s, q):
  global cnt
  cnt += 1
  q = deque() #큐 초기화
  for i in s:
    q.append(i)
  return q

#2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
def paste_smile(s, q):
  global cnt
  cnt += 1
  for i in q:
    s.append(i)
  return s

#3. 화면에 있는 이모티콘 중 하나를 삭제
def delete_smile(s):
  global cnt
  cnt += 1
  s.pop(-1)
  return s
  
  

def bfs():
  global cnt
  s = ['Smile'] #화면
  q = deque() #클립보드
  q = copy_screen(s, q)
  while q: #클립보드가 비어있지 않는 상태
    s = paste_smile(s, q) #화면에 붙여넣기
    
    if len(s) == S: return cnt
    
    # q = copy_screen(s, q) #큐에 화면에 있는 걸 복사
    
    #클립보드가 비어있는 상태에선 붙여넣기를 할 수 없다.
    
    #클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 했을 때, S개보다 작으면 붙여넣기 함
    if len(paste_smile(s, q)) < S: 
      if len(paste_smile(s, copy_screen(s, q))) < S: 
      s = paste_smile(s, q)
    else: delete_smile(s)
    
    
    
cnt = 0
S = int(input())
    
print(bfs())   



실패2 - 시간 초과
from collections import deque
import sys

def bfs():
  global S
  visited = [-1] * 100001
  q = deque()
  q.append([1, 0, 0]) #screen에 있는 이모티콘 개수, 클립보드에 복사된 이모티콘 개수, 시간의 최솟값
  
  while q:
    s, c, cnt = q.popleft()
    
    if s == S: return cnt
    #화면에 있는 이모티콘을 복사해서 클립보드에 저장한다. 이 때 덮어쓰기를 함
    if visited[s] == -1:   
      visited[s] = cnt
      q.append([s, s, cnt +1]) 
    #클립보드가 차 있을 때 화면에 클립보드의 모든 이모티콘을 붙여넣기 한다 
    if c != 0: 
      q.append([s + c, c, cnt + 1]) 
    #화면에 있는 이모티콘 중 하나를 삭제한다.
    if s > 0:
      q.append([s-1, c, cnt + 1])
      
S = int(input())
print(bfs())                       
'''