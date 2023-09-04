def f_cnt(y,x):
    s1 = getsum(y,x,m,4)
    s2 = getsum(y,x,m,8)
    return max(s1,s2)

def getsum(y,x,m,l):
    s = arr[y][x]
    for k in range(l-4,l):
        for t in range(1,m):
            dy = y + direct[k][0]*t
            dx = x + direct[k][1]*t
            if 0 <= dy < n and 0<=dx<n:
                s += arr[dy][dx]
    return s

direct = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    maxx = -21e8
    for i in range(n):
        for j in range(n):
            s = f_cnt(i,j)
            if s > maxx:
                maxx = s
    print(f"#{tc}",maxx)