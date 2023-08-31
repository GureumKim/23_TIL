"""

Topological Sort(위상 정렬),,, 큐 이용 --> BFS 느낌

"""

from collections import deque

name = ['A','B','C','D','E','F','G']
arr = [
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]

acc = [0] * 7  # 사전 작업 개수
for j in range(7):
    for i in range(7):
        if arr[i][j] == 1:
            acc[j] += 1

q = deque()
# 당장 사전 작업 없이 착 수 할 수 있는 작업 추가(삽입)
for i in range(7):
    if acc[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in range(7):
        if arr[now][i] == 1:  # 작업을 할 수 있을 때
            acc[i] -= 1
            if acc[i] == 0:  # 사전 작업 개수 0이라면
                q.append(i)  # 착수 가능

# BOJ 2252


from collections import deque

n, m = map(int, input().split())
edge = [[] for _ in range(n + 1)]  # 인접 리스트 생성
acc = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    acc[b] += 1
    edge[a].append(b)

q = deque()
for i in range(1, n + 1):
    if not acc[i]:
        q.append(i)
ans = []
while q:
    now = q.popleft()
    ans.append(str(now))
    for adj_node in edge[now]:
        acc[adj_node] -= 1
        if acc[adj_node] == 0:
            q.append(adj_node)
print(' '.join(ans))
