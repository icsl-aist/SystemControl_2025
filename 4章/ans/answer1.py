# answer.py
from control import tf, step_response
import numpy as np

def get_correct_step_response():
    P1 = tf([1, 3], [1, 3, 2])
    t = np.arange(0, 10, 0.01)
    y, t = step_response(P1, t)
    return y, t
