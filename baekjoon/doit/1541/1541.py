from queue import PriorityQueue

def solve(op, mystack):
    sum = 0
    part_sum = 0
    
    while op:
        a = mystack.pop()
        tmp_op = op.pop()

        if tmp_op == '+':
            part_sum += a
        elif tmp_op == '-':
            sum += (part_sum + a)*-1
            part_sum = 0

    sum += part_sum
    if mystack:
        sum += mystack.pop()

    return sum

def main():
    eq = []
    t=input()

    mystack = []
    op = []
    s = ''
    i=0
    while i<len(t):
        if t[i] == '+' or t[i] == '-':
            if s:
                mystack.append(int(s))
            op.append(t[i])
            s = ''
        else:
            s += t[i]
        i += 1
    if s:
        mystack.append(int(s))

    print(solve(op, mystack))


if __name__ == '__main__':
    main()