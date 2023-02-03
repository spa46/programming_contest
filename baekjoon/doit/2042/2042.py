import sys

n, m, k = map(int, sys.stdin.readline().split())

index = 1
while index<n:
    index*=2

arr = [0] * (index*2)

i = index
for _ in range(n):
    arr[i] = int(sys.stdin.readline())
    i += 1

def addTree(arr, index):
    if index <= 1:
        return

    i = index
    while i<index*2:
        arr[i//2] = arr[i] + arr[i+1]
        i+=2
    addTree(arr, index//2)

addTree(arr, index)

def modify(arr, b, c):
    arr[b] = c
    while b > 1:
        b = b-1 if b%2 == 1 else b
        arr[b//2] = arr[b] + arr[b+1]
        b = (b // 2)
    # print(arr)

def sumSegments(arr, b, c):
    sum = 0

    while b <= c:
        bp = b//2
        cp = c//2

        if b == c:
            sum += arr[b]

        if b%2 == 1 and bp != cp:
            sum += arr[b]
        b = bp + 1 if b % 2 == 1 else bp

        if c%2 == 0 and bp != cp:
            sum += arr[c]
        c = cp - 1 if c % 2 == 0 else cp

    print(sum)

# print(arr)
for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        modify(arr, index+b-1, c)
    else:
        # print(arr)
        sumSegments(arr, index+b-1, index+c-1)
# 1 - b->c
# 2 - b~c