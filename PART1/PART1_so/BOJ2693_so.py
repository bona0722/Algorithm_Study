#2693 N번째 큰 수

t = int(input())
a = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
  a[i] = sorted(a[i])
  print(a[i][-3])
