def solution(ability):
    max_sum = 0

    def dfs(arr, pos, sum):
        nonlocal max_sum

        if pos >= len(ability[0]):
            return max(max_sum, sum)

        for i in range(len(ability)):
            if i in arr:
                continue
            print(arr, i, pos, sum + ability[i][pos])

            max_sum = max(max_sum, dfs(arr + [i], pos + 1, sum + ability[i][pos]))

        return max_sum

    return dfs([], 0, 0)

a=solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])
print(a)