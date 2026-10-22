# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "seaborn>=0.13.2",
#     "numpy>=2.5.4",
# ]
# ///
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

os.makedirs("images", exist_ok=True)

def plot_walk(pattern: np.ndarray) -> None:
    X, Y = pattern[:, 0], pattern[:, 1]
    with sns.axes_style("darkgrid"):
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.scatter(X, Y, s=2, color="#088F8F", rasterized=True)
        ax.set(title="Random Walk with p = 1/4", xlabel="step i", ylabel="step j")
        fig.tight_layout()
        fig.savefig("images/random_walk.png", dpi=150, bbox_inches="tight", pad_inches=0)
    plt.close(fig)

def main() -> None:
    lines = sys.stdin.read().splitlines()[:-1]
    pattern = np.loadtxt(lines, dtype=np.int64)
    plot_walk(pattern)
    
if __name__ == "__main__":
    main()
