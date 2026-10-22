# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "numpy>=2.5.4",
# ]
# ///
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from matplotlib.collections import PatchCollection

def plot_thuemorse(pattern: np.ndarray) -> None:
    print(pattern)

def main() -> None:
    pattern = np.loadtxt(
        sys.stdin,
        dtype=str
    )
    plot_thuemorse(pattern)
    
if __name__ == "__main__":
    main()
