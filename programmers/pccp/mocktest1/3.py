Rr = ['RR', 'Rr', 'Rr', 'rr']

def solution(queries):
    def dfs(n, p):
        if n <= 1:
            return 'Rr'

        parent = (p) // 4
        child = (p) % 4

        res = dfs(n - 1, parent)
        if res == 'Rr':
            return Rr[child]
        elif res == 'rr':
            return 'rr'
        else:
            return 'RR'

    answer = []
    for n, p in queries:
        answer.append(dfs(n, p - 1))

    return answer