def solution(command):
    direction = ['N', 'E', 'S', 'W']
    curr = 0
    location = [0, 0]
    go = 1

    for v in command:
        if v == 'R':
            curr = (curr + 1) % 4
        elif v == 'L':
            curr = (curr - 1) % 4

        if v == 'G' or v == 'B':
            if v == 'G':
                go = 1
            elif v == 'B':
                go = -1

            if direction[curr] == 'N':
                location[1] += go
            elif direction[curr] == 'E':
                location[0] += go
            elif direction[curr] == 'S':
                location[1] -= go
            else:
                location[0] -= go

    location = list(location)
    return location