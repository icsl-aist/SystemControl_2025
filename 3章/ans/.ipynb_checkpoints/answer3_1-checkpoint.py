from control import ss

def get_correct_answer():
    A = [[1, 1, 2], [2, 1, 1], [3, 4, 5]]
    B = [[2], [0], [1]]
    C = [1, 1, 0]
    D = [0]
    return ss(A, B, C, D)
