# 핵심: 반으로 쪼갠다
# return 되는 때 혹은 함수 종료 조건 with 구하고자 하는 값

def rcp(a,b):
    if cards[a] == cards[b] or cards[a] - cards[b] == 1\
                                or cards[a] - cards[b] == -2:
        return a
    else:
        return b
    

def winner(start,end):
    if end - start <= 1:
        return rcp(start,end)
    
    g1 =  winner(start, (start+end)//2)
    g2 = winner((start+end)//2+1,end)
    return rcp(g1,g2)


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    cards = list(map(int,input().split()))
    print(f"#{tc} {winner(0,n-1)+1}")