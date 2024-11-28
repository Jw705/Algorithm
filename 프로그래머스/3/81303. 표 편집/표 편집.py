def solution(n, k, cmd):
    linked_list = {i : [i - 1, i + 1] for i in range(n)}
    linked_list[0][0] = None
    linked_list[n - 1][1] = None
    del_stack = []
    
    for c in cmd:
        if c[0] == 'U':
            X = int(c.split()[1])
            for _ in range(X):
                k = linked_list[k][0]
        elif c[0] == 'D':
            X = int(c.split()[1])
            for _ in range(X):
                k = linked_list[k][1]
        if c[0] == 'C':
            del_stack.append(k)
            prev, next_ = linked_list[k]
            if next_ is not None:
                linked_list[next_][0] = prev
                k = next_
            else:
                k = prev
            if prev is not None:
                linked_list[prev][1] = next_
        if c[0] == 'Z':
            target = del_stack.pop()
            prev, next_ = linked_list[target]
            if prev is not None:
                linked_list[prev][1] = target
            if next_ is not None:
                linked_list[next_][0] = target
    
    state = ['O'] * n
    for deleted_low in del_stack:
        state[deleted_low] = 'X'  
    
    answer = ''.join(state)    
    return answer