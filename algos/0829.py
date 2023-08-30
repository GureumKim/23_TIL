# 최대 공약수

# 1
a, b = map(int, input().split())
mx = 1
for i in range(1, min(a, b) + 1):
    if not a % i and not b % i:
        mx = i
print(mx)


# 2 유클리드 호제법(더 빠름)

def gcd(a, b):
    while b:
        temp = a % b
        a = b
        b = temp
    return a


a, b = map(int, input().split())
ans = gcd(a, b)
print(ans)
# 최소 공배수
print("lcm:", ans * (a // ans) * (b // ans))

# 약수

# 1
n = int(input())
for i in range(2, n + 1):
    for j in range(2, i):
        if not i % j: break
    else:
        print(i, end=' ')
print()

# 2 에라토스테네스의 체

n = int(input())
ans = [1] * (n + 1)
ans[:2] = [0] * 2
for i in range(2, int(n ** (1 / 2)) + 1):
    if not ans[i]: continue
    for j in range(2 * i, n + 1, i):
        ans[j] = 0
for i in range(2, n + 1):
    if ans[i]:
        print(i, end=' ')
print()

# import math
# math.sqrt() 사용 가능
import math
def erato(n):
    arr = [0]*(n+1)
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(2*i,n+1,i):
            arr[j] = 1
    for i in range(2,n+1):
        if not arr[i]:
            print(i,end=' ')
    print()
erato(20)

# Sliding Window
# key word = "연속되는" 구간합 !!

# 예, 연속되는 n개의 구간의 합 중 최대(최소)값을 구하시오

# 얘는 연속되는 개수-1만큼의 차를 내는 low, high pointer활용해서 둘 다 하나씩 늘려나가면 됨

# two pointer
# key word = "구간합"

# 슬라이딩 윈도우는 구간의 size가 정해짐
# two pointer는 구간의 size가 정해지지 않음

n, m = map(int, input().split())
nums = list(map(int, input().split()))

p1 = p2 = 0
s = cnt = 0

while p2 < n:
    s += nums[p2]
    p2 += 1

    if s > m:
        while s > m:
            s -= nums[p1]
            p1 += 1
    if s == m:
        cnt += 1
print(cnt)

#  방법 2

n, m = map(int, input().split())
nums = list(map(int, input().split()))

l = h = 0
s = cnt = 0

while 1:
    if s >= m or h==n:
        s -= nums[l]
        l += 1
    elif s<m:
        s+=nums[h]
        h+=1
    if s == m:
        cnt+=1
    if l == n:
        break
print(cnt)

# 10 5
# 1 2 3 4 2 5 3 1 1 5
