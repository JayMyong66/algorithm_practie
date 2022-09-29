lst = [1,1,2,2,2,8]
num = list(map(int, input().split()))
result = []

for i in range(len(lst)):
    result.append(lst[i] - num[i])

for i in range(len(result)):
    print(result[i], end=' ')

# 체스 말 수 - 입력 받은 수를 한줄로 print 함!