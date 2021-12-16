import re
import numpy as np
def check(reply):
    control = np.array([1,2,2,2,3,4,6,10])
    numbers = np.array(re.findall('[0-9]+', reply), dtype=int)
    if len(numbers) != len(control):
        return False
    return all(numbers[i] <= control[i] for i in range(len(numbers))) or all(numbers[i] >= control[len(numbers) - i - 1] for i in range(len(numbers)))