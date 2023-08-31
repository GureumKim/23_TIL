
#13863
def haspath(y, x):
    global flag
    for k in range(4):
        di = dy[k] + y
        dj = dx[k] + x
        if di < 0 or dj < 0 or di >= n or dj >= n:
            continue
        if m[di][dj] == '3':
            flag = 1
            return
        elif m[di][dj] == '0':
            m[di][dj] = 1
            haspath(di, dj)
 
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
t = int(input())
for tc in range(1, t + 1):
    flag = 0
    n = int(input())
    m = [list(input()) for _ in range(n)]
     
    jump = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] == '2':
                y = i
                x = j
                jump = 1
                break
        if jump:
            break
     
    print(f"#{tc}", end=' ')
    haspath(y, x)
     
    if flag:
        print("1")
    else:
        print("0")



# 15036
def has_path(s,g):
    if s == g:
        return 1
    if paths[s]:
        for i in paths[s]:
            if visited[i]:continue
            visited[i] = 1
            if has_path(i,g):
                return 1
    return 0
 
t = int(input())
for tc in range(1,t+1):
    V, E = map(int,input().split())
    paths = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        s,g = map(int,input().split())
        paths[s].append(g)
     
    s, g = map(int,input().split())
    visited[s] = 1
    print(f"#{tc}", end=' ')
    if has_path(s,g):
        print(1)
    else:
        print(0)




