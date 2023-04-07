import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 558620654 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    S = np.sqrt(1/(len(x)-1)*np.sum((x-x.mean())**2))
    z2 = norm.ppf(1-alpha/2)
    z1 = norm.ppf(alpha/2)
    left = 2*x.mean()+2*z1*S/np.sqrt(len(x))
    right = 2*x.mean()+2*z2*S/np.sqrt(len(x))
    return left, right
