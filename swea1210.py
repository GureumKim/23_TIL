def up(y,x):
    while y>0:
         
        if x < 99:
            if F[y][x+1] == 1:
                x += 1
                y, x = right(y,x)
                continue
     
        if 0 < x:
            if F[y][x-1] == 1:
                x -= 1
                y, x =left(y,x)
                continue
        y -= 1
        if y == 0:
           return x
    return x
 
     
def right(r,c):
    while c<99:
        if F[r-1][c+1] == 1:
            return r-1, c+1
        c +=1
    return r-1, c
 
 
def left(r,c):
    while 0<c:
        if F[r-1][c-1] == 1:
            return r-1, c-1
        c -= 1
    return r-1, c
 
 
for _ in range(10):
    tno = int(input())
    F = [list(map(int,input().split())) for _ in range(100)]
    for e_x in range(100):
        if F[99][e_x] == 2:
            s_x = up(99,e_x)
            print(f"#{tno} {s_x}")
            break