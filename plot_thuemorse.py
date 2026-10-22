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
    fig, ax = plt.subplots()

    ax.imshow(
        pattern == "+",
        cmap="binary",
        interpolation="nearest",
        origin="upper"
    )

    ax.set_axis_off()
    fig.savefig(
        "images/thue_morse.png",
        dpi=150,
        bbox_inches="tight",
        pad_inches=0
    )
    plt.close(fig)

def main() -> None:
    pattern = np.loadtxt(
        sys.stdin,
        dtype=str
    )
    plot_thuemorse(pattern)
    
if __name__ == "__main__":
    main()
