import math

# x = N제곱 꼴 = 거의 소수
# a <= x <= b

# 2초
# 1<=A<=B<=10의 14승
# 100000000000000

# N>=2
# 10의 7승
# 10000000

# 1 10
#  2의 제곱: 4, 8
#  3의 제곱: 9
# 3개

# 소수 구하기
#N = a*b
#25 = 5*5
#N = a(제곱근의 N) * b

# 제곱근 구하기
# 구해진 소수들을 상대로 구역 안에 있는 제곱근을 탐색
# 2,3,5,7
# 예제: 100 200 의 거의 제곰을 찾으라
# 2,4,8,16,32,64,128,256
# 3,9,27,81,243
# 5,25,125
# 7,49,343
# 11, 121
# 13, 169
# 17, 289

# 각각의 소수들을 iteration



# 1 10
#  2의 제곱: 4, 8
#  3의 제곱: 9
# 3개

def solve(m,n):
    arr = [1] * 10000001
    arr[0] = 0;
    arr[1] = 0
    prime = []

    for i in range(2, int(math.sqrt(n)) + 1):
        if not arr[i]:
            continue

        for j in range(i + i, int(math.sqrt(n)) + 1, i):
            arr[j] = 0
            j += 1

    cprime = []
    cnt_prime = 0
    for i in range(int(math.sqrt(n)) + 1):
        if arr[i]:
            j = i * i

            while j <= n:
                if j >= m:
                    if j not in cprime:
                        cprime.append(j)
                        cnt_prime += 1
                j *= i

    return cnt_prime


if __name__ == '__main__':
    m,n = map(int, input().split())

    print(solve(m,n))

