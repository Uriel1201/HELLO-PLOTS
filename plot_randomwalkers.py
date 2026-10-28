# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "polars>=2.1.0",
#     "pyarrow>=26.0.0",
#     "seaborn>=0.13.2",
# ]
# ///

import sys
import os
import matplotlib.pyplot as plt
import seaborn           as sns
import numpy             as np
import pyarrow           as pa
import polars            as pl

os.makedirs("images", exist_ok=True)

def plot_mass(x_label: str, x: pl.Series) -> None:
    plt.hist(x, bins=50, density=True)
    plt.axvline(x.mean(), color="red", linestyle="--", label="mean")
    plt.axvline(np.median(x), color="gray", linestyle="--", label="median")
    plt.xlabel(x_label)
    plt.ylabel("density")
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/randomwalkers.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

def plot_line(x_label: str,
    x: pl.Series,
    y_label: str,
    y: pl.Series
) -> None:
    plt.figure(figsize = (9, 7))
    sns.set(style= 'darkgrid')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    sns.lineplot(x = x, y = y, color = '#088F8F', marker = 'o')
    plt.tight_layout()
    plt.savefig("images/large_numbers.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

def main() -> None:
    data = sys.stdin.buffer.read()
    if not data:
        sys.exit(1)
    with pa.ipc.open_stream(pa.py_buffer(data)) as reader:
        table = reader.read_all()
    pl.Config.set_tbl_width_chars(150)
    df     = pl.from_arrow(table)
    name_0 = table.column_names[0]
    name_1 = table.column_names[1]
    name_2 = table.column_names[2]
    trials = df[name_0]
    steps  = df[name_1]
    means  = df[name_2]
    plot_mass(name_1, steps)
    plot_line(name_0, trials, name_2, means)
    print(df.head(2))
    print(f"Average Number of Steps: {df[name_2][-1]}")

if __name__ == "__main__":
    main()
