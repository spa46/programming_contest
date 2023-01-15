import math

N = 10000001

def solve(n):


def solve(n):
    def gcd(a,b):
        if b%a == 0:
            return a
        elif a%b == 0:
            return b
        if a>b:
            return gcd(a%b,b)
        else:
            return gcd(b%a,a)

    cnt = 1
    for i in range(2, n+1):
        if gcd(n,i) == 1:
            cnt += 1

    return cnt

def main():
    n = int(input())
    print(solve2(n))


if __name__ == '__main__':
    main()