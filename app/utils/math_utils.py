import numpy as np

def softmax(x: np.ndarray) -> np.ndarray:
    """Compute softmax values."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def normalize(value: float, min_val: float = 0, max_val: float = 1) -> float:
    """Normalize value to [0, 1]."""
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0.5

def clamp(value: float, low: float = 0, high: float = 1) -> float:
    """Clamp value to range."""
    return max(low, min(high, value))
