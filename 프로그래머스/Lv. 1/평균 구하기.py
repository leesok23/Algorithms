# Version 1
def solution(arr):
    return sum(arr) / len(arr)


# Version 2
import numpy as np

def solution(arr):
    return np.mean(arr)
