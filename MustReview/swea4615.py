t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    pan = [[0]*(n+1) for _ in range(n+1)]
    mid = n//2
    pan[mid][mid] = pan[mid+1][mid+1] = 2
    pan[mid][mid+1] = pan[mid+1][mid] = 1
 
    for _ in range(m):
        x,y,c = map(int,input().split())
        pan[y][x] = c
        for di,dj in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
            turn = []
            for k in range(1,n):
                dy,dx = y + di*k, x+dj*k
                if dy<1 or dx<1 or dy>n or dx>n:break
                if pan[dy][dx] == 0: break
                elif pan[dy][dx] == c:
                    while turn:
                        ty,tx = turn.pop()
                        pan[ty][tx]=c
                    break
                else:
                    turn.append((dy,dx))
 
    black = white = 0
    for lst in pan:
        black += lst.count(1)
        white += lst.count(2)
    print(f"#{tc}",black,white)