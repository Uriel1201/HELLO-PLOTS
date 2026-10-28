# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "seaborn>=0.13.2",
#     "numpy>=2.5.4",
#     "pyarrow>=26.0.0",
#     "polars>=2.1.0",
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

def plot_walk(x: np.ndarray, y: np.ndarray, *, x_title: str, y_title: str) -> None:
    with sns.axes_style("darkgrid"):
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.scatter(x, y, s=2, color="#088F8F", rasterized=True)
        ax.set(title="Random Walk; p = 1/4", xlabel=x_title, ylabel=y_title)
        fig.tight_layout()
        fig.savefig("images/random_walk.png", dpi=150, bbox_inches="tight", pad_inches=0)
    plt.close(fig)

def main() -> None:
    data = sys.stdin.buffer.read()
    if not data:
        sys.exit(1)
    with pa.ipc.open_stream(pa.py_buffer(data)) as reader:
        table = reader.read_all()
    pl.Config.set_tbl_width_chars(150)
    x_name = table.column_names[0]
    y_name = table.column_names[1]
    x = table[x_name].chunk(0).to_numpy(zero_copy_only=True)
    y = table[y_name].chunk(0).to_numpy(zero_copy_only=True)
    plot_walk(x, y, x_title=x_name, y_title=y_name)
    print(pl.from_arrow(table))

if __name__ == "__main__":
    main()
