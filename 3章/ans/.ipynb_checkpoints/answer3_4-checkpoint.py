# answer.py

from control import tf, feedback, series

def get_correct_answer():
    S1 = tf(1, [1, 1])
    S2 = tf(1, [1, 2])
    S3 = tf([3, 1], [1, 0])
    S4 = tf([2, 0], [0, 1])
    S12 = feedback(S1, S2)
    S123 = series(S12, S3)
    S = feedback(S123, S4)
    return S
    
