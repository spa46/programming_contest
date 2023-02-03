import sys

n, m = map(int, sys.stdin.readline().split())

index = 1
while index < n:
    index*= 2

arr = [sys.maxsize]*((index*2) + 1)
for i in range(n):
    j = index+i
    arr[j] = int(sys.stdin.readline())


def minTree(arr, index):
    if index < 1:
        return

    i = index
    while i<index*2:
        arr[i//2] = min(arr[i], arr[i+1])
        i += 2
    minTree(arr, index//2)

minTree(arr, index)

def findMin(arr, i, j):
    if i>j:
        return sys.maxsize

    mmin = sys.maxsize
    if i%2 == 1:
        mmin = min(mmin, arr[i])
        i+=1
    if j%2 == 0:
        mmin = min(mmin, arr[j])
        j-=1

    mmin = min(mmin, findMin(arr, i//2, j//2) )
    return mmin

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(findMin(arr, index+i-1, index+j-1))


