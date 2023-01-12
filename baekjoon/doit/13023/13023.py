import sys

# dfs
# 0부터 traverse를 하는데 깊이가 5여야 함
#
# dfs(v):
#     if not Node 또는 노드가 4를 만나면 리턴
#     모든 Node를 Traverse
#     if not visited(second node):
#       반환

def dfs(v, d):
    if v == '4':
        return 0



if __name__ == '__main__':
    n,m = map(int, input().split())
    d = {}
    v = [False]*n
    arr = []
    for i in range(m):
        i,j = map(int, input().split())

        if i not in d:
            d[i] = [j]
        else:
            d[i].append(j)
        if j not in d:
            d[j] = [i]
        else:
            d[j].append(i)
    dfs(d)
