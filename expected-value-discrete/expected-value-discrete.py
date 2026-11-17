import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    expected=0
    for i in range(len(x)):
        expected +=x[i] * p[i]
        
    return float(expected)