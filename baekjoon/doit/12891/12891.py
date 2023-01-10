import sys

# {‘A’, ‘C’, ‘G’, ‘T’}
# 부분문자열에서 등장하는 문자의 개수가 특정 개수 이상

# 부분 문자열을 슬라이딩 윈도우로
# CAGT 카운트를 동시에 할 것

# i초기화, j초기화
# i-j까지 슬라이딩 윈도우를 채워놓고
# Iteration 하면서 하나씩 체크
# |CCTGGATT|G
# A:1 C:2 G:2 T:3
# O(N)

# A: arr[0]
# C: arr[1]
# G: arr[2]
# P: arr[3]

def get_dna(ch, ss):
    if ch == 'A':
        ss[0] += 1
    elif ch == 'C':
        ss[1] += 1
    elif ch == 'G':
        ss[2] += 1
    elif ch == 'T':
        ss[3] += 1

def remove_dna(ch, ss):
    if ch == 'A':
        ss[0] -= 1
    elif ch == 'C':
        ss[1] -= 1
    elif ch == 'G':
        ss[2] -= 1
    elif ch == 'T':
        ss[3] -= 1

def solve(p, str, req):
    ss = [0, 0, 0, 0]
    cnt = 0

    i=0; j=0;
    while j<p:
        get_dna(str[j], ss)
        j+=1

    if req[0] <= ss[0] and req[1]<=ss[1] and req[2]<=ss[2] and req[3]<=ss[3]:
        cnt += 1

    while j<len(str):
        get_dna(str[j], ss)
        remove_dna(str[i], ss)

        if req[0] <= ss[0] and req[1]<=ss[1] and req[2]<=ss[2] and req[3]<=ss[3]:
            cnt += 1
        
        i+=1; j+=1

    return cnt

def main():
    s,p = map(int, input().strip().split())
    str = input()
    req = list(map(int, input().split()))
    print(solve(p, str, req))

if __name__ == '__main__':
    main()
