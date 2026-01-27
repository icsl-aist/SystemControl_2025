# answer4_2.py
from control import tf, step_response
import numpy as np

def get_correct_step_response():
    P2 = tf([0, 1], [1, 2, 2, 1])
    t = np.arange(0, 15, 0.01)
    y, t = step_response(P2, t)
    return y, t
