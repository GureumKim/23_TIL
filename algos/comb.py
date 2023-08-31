# def comb(n,r):          # nCr 조합 경우 출력
#     global cnt
#     if r == 0:      # r개 조합 다 만들면 출력
#         print(*choice)
#         cnt += 1
#         return
#     elif n < r: # 남은 원소보다 골라야할 가짓수가 더 많다면 return
#         return
#     choice[r-1] = hubo[n-1] # index 뭘로 둬야할지 잘 보기
#     comb(n-1,r-1) # 조합 만드는 거 계속
#     comb(n-1,r) # 선택한 거 빼고 다시 r개 조합
#
#
# cnt = 0
# hubo = [*range(5)]
# r = 3
# # print(hubo)
# choice = [0]*r
# comb(len(hubo),r)
# print("\n조합 개수:",cnt,"개")


# 넣는 겨우 빼는 경우 분기(line 36)
# def subset(N,level=0):
#     if level==N:
#         s =0
#         for i in range(N):
#             if bit[i]:
#                 s += arr[i]
#         if s == 0:
#             for i in range(N):
#                 if bit[i]:
#                     print(arr[i],end=' ')
#             print()
#         # return
#
#     else:
#         bit[level] =1 # 포함 시킬 때
#         subset(N,level+1)
#         bit[level] = 0 # 뺄 때
#         subset(N,level+1)
#     return # if 수행되면 자동으로 여기로 옴

def subset(i,N):
    global cnt
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s+=arr[j]
        if s != 0:
            cnt += 1
            for j in range(N):
                if bit[j]:
                    print(arr[j], end=' ')
            print()

    else:
        bit[i] = 1
        subset(i+1,N)
        bit[i] = 0
        subset(i+1,N)
    return


arr = [*range(1,11)]
cnt = 0
n = len(arr)
bit=[0]*n
subset(0,n)
print("\n",cnt,sep='')


def subset(i,N,s,c):
    if s == 0 and c!=0: #부분집합에 0이 있다면 1(True), c=0은 공집합일 때!
        return 1
    elif i == N:
        return 0
    else:
        if subset(i+1,N,s+arr[i],c+1): #부분집합 만들어감
            return 1
        if subset(i+1,N,s,c):
            return 1
        return 0

arr = [1,2,3]
N = len(arr)
bit = [0]*N
cnt = 0
print(subset(0,N,0,0))