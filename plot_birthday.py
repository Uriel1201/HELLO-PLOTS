# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "seaborn>=0.13.2",
#     "numpy>=2.5.4",
#     "pyarrow>=26.0.0",
#     "polars>=1.44.1",
# ]
# ///
import os
import sys
import matplotlib.pyplot as plt
import seaborn           as sns
import numpy             as np
import pyarrow           as pa
import polars            as pl

os.makedirs("images", exist_ok=True)

def plot_dist(index: np.ndarray, p:np.ndarray) -> None:
    plt.figure(figsize = (7, 9))
    sns.set_theme(style = 'darkgrid')
    plt.title(f'P_X(x) = 0.50')
    plt.xlabel(f'x')
    plt.ylabel(f'Distribution Function')
    sns.scatterplot(x = index,
        y = p,
        color = '#088F8F'
    )
    f_x = index[-1]
    f_y = p[-1]
    plt.text(x = f_x,
        y = f_y,
        s = f'{f_x}',
        color = '#8f0808',
        ha = 'right',
        va = 'baseline'
    )
    plt.axhline(y = 0.5,
        color = '#8f0808',
        linestyle = ':'
    )
    plt.tight_layout()
    plt.savefig("images/birthday_dist.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

def plot_freq(index: np.ndarray, freq: np.ndarray) -> None:
    plt.bar(index, freq)
    plt.xlabel("X = x")
    plt.ylabel("FREQUENCIES")
    plt.tight_layout()
    plt.savefig("images/birthday_freq.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

def main() -> None:
    with pa.ipc.open_stream(sys.stdin.buffer) as reader:
        table = reader.read_all()
    pl.Config.set_tbl_width_chars(150)
    df    = pl.from_arrow(table)
    index = table["k"].chunk(0).to_numpy(zero_copy_only=True)
    p     = table["p_k"].chunk(0).to_numpy(zero_copy_only=True)
    freq  = table["frequency"].chunk(0).to_numpy(zero_copy_only=True)
    print(df)
    plot_dist(index, p)
    plot_freq(index, freq)

if __name__ == "__main__":
    main()
