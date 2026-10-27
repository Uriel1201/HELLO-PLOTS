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
import sys
import os
import matplotlib.pyplot as plt
import seaborn           as sns
import numpy             as np
import pyarrow           as pa
import polars            as pl

os.makedirs("images", exist_ok=True)

def plot_dist(title: str, index_array: np.ndarray) -> None:
    plt.figure(figsize = (9, 7))
    sns.set_theme(style= 'darkgrid')
    plt.title(f'{title}')
    plt.ylabel("Frequency")
    plt.xlabel("index")
    sns.countplot(x = index_array,
        color = '#088F8F'
    )
    plt.tight_layout()
    plt.savefig("images/dis_dist.png",
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
    col_name = table.column_names[0]
    sample = table[col_name].chunk(0).to_numpy(zero_copy_only=True)
    plot_dist(col_name, sample)
    print(pl.from_arrow(table))
    
if __name__ == "__main__":
    main()
