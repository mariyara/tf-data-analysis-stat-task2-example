import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import expon


chat_id = 558620654 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha=1-p
    y = x-0.032
    #e1+e2=1-p
    e1=alpha/2
    e2=1-alpha/2
    n=len(y)
    left = np.max(y)/(e2)**(1/n)+0.032
    right = np.max(y)/(e1)**(1/n)+0.032

    return left, right
