def solution(X, Y, D):
    jump = (Y - X) // D
    if X + jump * D < Y:
        jump += 1
    return jump