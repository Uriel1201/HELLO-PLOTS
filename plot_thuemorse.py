# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "numpy>=2.5.4",
# ]
# ///
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from matplotlib.collections import PatchCollection

os.makedirs("images", exist_ok=True)

def plot_thuemorse(pattern: np.ndarray) -> None:
    patches_list = []
    fig, ax = plt.subplots()
    n = pattern.shape[0]
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    for i in range(pattern.shape[0]):
        for j in range(pattern.shape[1]):
            color = "black" if pattern[i, j] == "+" else "white"
            r = pch.Rectangle((j, i), 1, 1, facecolor=color)
            patches_list.append(r)
    patch_collection = PatchCollection(patches_list, match_original = True)
    ax.add_collection(patch_collection)
    plt.title(f"Thue-Morse Sequence")
    plt.show()

def main() -> None:
    pattern = np.loadtxt(
        sys.stdin,
        dtype=str
    )
    plot_thuemorse(pattern)
    
if __name__ == "__main__":
    main()
