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

def plot_dist(index_array: np.ndarray) -> None:
    plt.figure(figsize = (9, 7))
    sns.set_theme(style= 'darkgrid')
    plt.title(f'Frequencies')
    plt.ylabel(f'Frequency')
    plt.xlabel(f'index')
    sns.countplot(x = index_array, 
        color = '#088F8F'
    )
    plt.tight_layout()
    plt.savefig("images/discret_distribution.png", 
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

def main() -> None:
    index_array = np.loadtxt(
        sys.stdin,
        dtype=np.int64
    )
    plot_dist(index_array)
    
if __name__ == "__main__":
    main()
