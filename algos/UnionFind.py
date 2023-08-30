# # Q.1 문자 2개 입력 받은 후 두 문자가 같은 그룹인지 아닌지 출력
arr = [0]*200       #소문자 a의 ascii code = '97' 넉넉하게 200칸 배열 만들기(문자열 가지고 푸는 문제)

def findroot(member):
    # global arr
    if arr[ord(member)] == 0:    # 자기가 보스면 리턴
        return member
    return findroot(arr[ord(member)])

def union(a,b):
    """
    루트가 같으면 그룹화, 아니면 그룹화 x
    따라서 먼저 보스를 찾아줘야 함 => findroot(a)
    """
    # global arr
    fa,fb = findroot(a),findroot(b)
    if fa == fb:
        return
    arr[ord(fb)] = fa

union('a','b')
union('d','e')
union('b','e')
union('b','d')
union('e','f')

y,x = input().split()
if findroot(y) == findroot(x):
    print("same group")
else:
    print("different group")


# union-find 활용 graph에서 cycle 발생 여부 확인 가능

def findroot(x):
    if arr[ord(x)] == 0:
        return x
    # 아래처럼하면 경로 단축 가능
    ret = findroot(arr[ord(x)])
    arr[ord(x)]=ret  # 걍 자식 혹은 member에도 바로 보스가 ret이라고 넣어줘 버림, 경로 탐색 빨라짐!!!
    return ret

def union(a,b):
    fa, fb = findroot(a), findroot(b)
    if fa==fb:
        return -1
    arr[ord(fb)] = fa

arr = [0]*200
n,m = map(int,input().split())
for i in range(m):          # 간선 개수다, n 아니다!!!
    a, b = input().split()
    if union(a, b):
        print("cycle 발견");break
else:
    print("cycle 없음")


# Q.3 Kruskal
def findroot(x):
    if arr[ord(x)] == 0:
        return x
    ret = findroot(arr[ord(x)])
    arr[ord(x)]=ret
    return ret
def union(a,b):
    fa, fb = findroot(a),findroot(b)
    if fa == fb:
        return 0
    arr[ord(fb)] = fa
    return 1

n, m = map(int,input().split())
arr = [0]*200
lst = []
for _ in range(m):
    s,e,c = input().split()
    c = int(c)
    lst.append((s,e,c))
lst.sort(key = lambda x:x[-1])
cnt = 0
cost = 0
for i in range(m):
    s,e,c = lst[i]
    if union(s,e):
        cnt += 1
        cost += c

    if cnt == n-1:
        print(cost)
        break


# 2번 풀이
n,m=map(int,input().split())
lst=[list(input().split()) for _ in range(m)]
group=[0]*200
lst.sort(key=lambda x:int(x[2]))

def findroot(a):
    if not group[ord(a)]:
        return a
    ret=findroot(group[ord(a)])
    group[ord(a)]=ret
    return ret

def union(x,y,i):
    global group,total,cnt
    x_root,y_root=findroot(x),findroot(y)
    if x_root==y_root:
        return
    cnt+=1
    total+=int(lst[i][2])
    group[ord(y_root)]=x_root

total=0  # 총 비용
cnt=0   # 연결시킨 선의 개수

for i in range(m):
    if cnt==n-1:
        print(total)
        break
    union(lst[i][0],lst[i][1],i)
