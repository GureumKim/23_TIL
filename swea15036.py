def has_path(links,start,end,visited):
    if start == end:
        return 1
    visited[start] = True
    for i in links[start]:
        if not visited[i]: # visited == False
            if has_path(links, i, end, visited):
                return 1
 
 
t = int(input())
for tc in range(1,t+1):
    V, E = map(int,input().split())
    links = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
 
    for _ in range(E):
        a,b = map(int,input().split())
        links[a].append(b)
 
    S, G = map(int,input().split())
    print(f"#{tc}", end=' ')
    if has_path(links,S,G,visited):
        print("1")
    else:
        print("0")