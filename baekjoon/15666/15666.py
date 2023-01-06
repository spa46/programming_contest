import sys

def nm(m, nums):
    def dfs(arr, pos):
        if pos>=m:
            print(' '.join(map(str, arr)))
            return

        for v in nums:
            if not arr:
                dfs([v], pos + 1)
            elif arr[-1]<=v:
                dfs(arr+[v], pos+1)

    nums = list(set(nums))
    nums.sort()

    dfs([], 0)

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    nm(M, nums)


if __name__ == '__main__':
    main()