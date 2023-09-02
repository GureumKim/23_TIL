"""각 비트 반전 시킨 2진수 만들기"""

# binary = int(A,2) #1001 이런거 문자로 받아서 2진수 변환
# bin_list = [0]*N # 각 비트를 반전시킨 수 N개 저장 ( []에 append해도 ok )
# for i in range(N):
#     bin_list[i] = binary ^ (a<<i)

"""부분 수열의 합"""
t = int(input())
for tc in range(1,t+1):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    cnt = 0 #합이 K가 되는 경우의 수
    for i in range(1<<n): # 부분집합을 표시하는 i
        s = 0
        for j in range(n):  #j번 비트
            if i&(1<<j):    # i의 j번 비트 검사
                s += arr[j] # 0이 아니면 j번 원소가 부분집합에 포함됨
        if s == k:
            cnt += 1
    print(f"#{tc} {cnt}")

# 2번 풀이 아래 함수 이용

def f(i,n,s,k):
    global cnt
    if i == n:
        if s ==k:
            cnt += 1
    elif s >k:      # 백트래킹!! 근데 백트래킹 한다고 항상 무조건 좋아지는 것은 아님, 최악의 경우가 있다...
        return
    else:
        f(i+1,n,s+arr[i],k)
        f(i+1,n,s,k)
t = int(input())
for tc in range(1,t+1):
    n,k = map(int(input().split()))
    arr = list(map(int,input().split()))
    cnt = 0

    f(0,n,0,k)
    print(f"#{tc} {cnt}")


# 1
a = input()
b = input()
l1 = len(a)
l2 = len(b)
if l1 != l2:
    print("불가")
else:
    cnt1 = dict()
    cnt2 = dict()

    for e in a:
        if cnt1.get(e):
            continue
        else:
            cnt1[e] = a.count(e)

    for e in b:
        if cnt2.get(e):
            continue
        else:
            cnt2[e] = b.count(e)

    if cnt1 == cnt2:
        print("가능")
    else:
        print("불가")

# 2

a = input()
b = input()
l1 = len(a)
l2 = len(b)

cnt1 = dict()
cnt2 = dict()

for e in a:
    if cnt1.get(e):
        continue
    else:
        cnt1[e] = a.count(e)
for e in b:
    if cnt2.get(e):
        continue
    else:
        cnt2[e] = b.count(e)
ans = 0
if l1 != l2:
    ans += abs(l1-l2)
for e in a:
    if cnt2.get(e):
       ans += abs(cnt2.get(e)-cnt1.get(e))
    else: ans += cnt1.get(e)
for e in b:
    if not cnt1.get(e):
        ans += cnt2.get(e)
print(ans,"개",sep='')



# 3
s1 = input()
s2 = input()

s1 = sorted(s1)
# s2 = sorted(s2) 여기서 말고

l1 = len(s1)
l2 = len(s2)

cnt = 0

for i in range(l2-l1+1):
    print(sorted(s2[i:i+l1]))
    if s1 == sorted(s2[i:i+l1]):       #여기서
        cnt += 1
print(cnt,'개',sep='')