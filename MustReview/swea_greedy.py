def win(cnts,idx):
    if cnts[idx] == 3:
        return 1
    for i in (idx-2,idx-1, idx): #연속하는 거 체크
        if 0<=i<=7 and cnts[i] and cnts[i+1] and cnts[i+2]:
            return 1
    return 0
 
t = int(input())
for tc in range(1,t+1):
    cards = list(map(int,input().split()))
    # 빈도수 배열 사용
    # 1. 0-9까지(0<= <=7범위에서 check) or 2. 0-11까지 [dummy 생성]
    cnts1 = [0]*10
    cnts2 = [0]*10
 
    w = 0
    for i in range(12):
        if i%2 == 0:
            cnts1[cards[i]] += 1
            if win(cnts1,cards[i]):
                w = 1
                break
        else:
            cnts2[cards[i]] += 1
            if win(cnts2,cards[i]):
                w = 2
                break
 
    print(f"#{tc} {w}")