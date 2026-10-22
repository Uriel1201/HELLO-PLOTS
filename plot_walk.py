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

def plot_walk() -> None:
        X = np.array(x, dtype = int)
        Y = np.array(y, dtype = int)
        plt.figure(figsize = (9, 7))
        sns.set(style= 'darkgrid')
        plt.title(f'Random Walk with p = 1/2')
        plt.xlabel(f'step i')
        plt.ylabel(f'step j')
        sns.scatterplot(x = X, y = Y, color = '#088F8F', marker = 'o')
        plt.tight_layout()
        plt.show()
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
        dtype=np.int64
    )
    plot_thuemorse(pattern)
    
if __name__ == "__main__":
    main()
