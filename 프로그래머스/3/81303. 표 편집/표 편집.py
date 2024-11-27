def solution(n, k, cmd):
    # 연결 리스트: 각 행의 이전/다음 행을 저장
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    linked_list[0][0] = None  # 첫 행의 이전은 없음
    linked_list[n - 1][1] = None  # 마지막 행의 다음은 없음
    
    del_stack = []  # 삭제된 행 스택
    current = k  # 현재 선택된 행
    
    for c in cmd:
        if c[0] == 'U':  # 'U X': 위로 X칸
            X = int(c.split()[1])
            for _ in range(X):
                current = linked_list[current][0]
        elif c[0] == 'D':  # 'D X': 아래로 X칸
            X = int(c.split()[1])
            for _ in range(X):
                current = linked_list[current][1]
        elif c[0] == 'C':  # 'C': 현재 행 삭제
            prev, next_ = linked_list[current]
            del_stack.append((current, prev, next_))  # 삭제된 행 저장
            
            if prev is not None:
                linked_list[prev][1] = next_  # 이전 행의 다음을 현재 행의 다음으로 연결
            if next_ is not None:
                linked_list[next_][0] = prev  # 다음 행의 이전을 현재 행의 이전으로 연결
            
            # 현재 행 갱신
            current = next_ if next_ is not None else prev
        elif c[0] == 'Z':  # 'Z': 가장 최근 삭제된 행 복구
            node, prev, next_ = del_stack.pop()
            if prev is not None:
                linked_list[prev][1] = node  # 이전 행과 복구된 행 연결
            if next_ is not None:
                linked_list[next_][0] = node  # 다음 행과 복구된 행 연결
    
    # 최종 상태 구성
    result = ['O'] * n
    for node, _, _ in del_stack:  # 삭제된 행은 'X'로 표시
        result[node] = 'X'
    return ''.join(result)
