def solution(commands):
    answer = []
    table = [['EMPTY' for _ in range(51)] for _ in range(51)]
    parent = [[(i, j) for j in range(51)] for i in range(51)]

    for i in range(len(commands)):
        cmd = list(commands[i].split())
        if cmd[0] == 'UPDATE':
            if len(cmd) == 4:
                r, c, value = int(cmd[1]), int(cmd[2]), cmd[3]
                pr, pc = parent[r][c]
                table[pr][pc] = value
            else:
                value1, value2 = cmd[1], cmd[2]
                for j in range(1, 51):
                    for k in range(1, 51):
                        if table[j][k] == value1:
                            table[j][k] = value2
        elif cmd[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, cmd[1:])
            pr1, pc1 = parent[r1][c1]
            pr2, pc2 = parent[r2][c2]
            if table[pr1][pc1] == 'EMPTY':
                table[pr1][pc1] = table[pr2][pc2]
            for i in range(1, 51):
                for j in range(1, 51):
                    if parent[i][j] == (pr2, pc2):
                        parent[i][j] = (pr1, pc1)

        elif cmd[0] == 'UNMERGE':
            r, c = int(cmd[1]), int(cmd[2])
            pr, pc = parent[r][c]
            value = table[pr][pc]
            for i in range(1, 51):
                for j in range(1, 51):
                    if parent[i][j] == (pr, pc):
                        parent[i][j] = (i, j)
                        table[i][j] = 'EMPTY'
            table[r][c] = value
        elif cmd[0] == 'PRINT':
            r, c = int(cmd[1]), int(cmd[2])
            pr, pc = parent[r][c]
            value = table[pr][pc]
            answer.append(value)

    return answer
