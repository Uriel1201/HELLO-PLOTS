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

def plot_dist(
    index_label: str,
    index:       pl.Series, 
    p_label:     str,
    p:           pl.Series
) -> None:
    plt.figure(figsize = (7, 9))
    sns.set_theme(style = 'darkgrid')
    plt.xlabel(index_label)
    plt.ylabel(p_label)
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

def plot_freq(
    index_label:       str, 
    index:             pl.Series,
    frequencies_label: str,
    frequencies:       pl.Series
) -> None:
    plt.bar(index, frequencies)
    plt.xlabel(index_label)
    plt.ylabel(frequencies_label)
    plt.tight_layout()
    plt.savefig("images/birthday_freq.png",
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
    name_0      = table.column_names[0]
    name_1      = table.column_names[1]
    name_2      = table.column_names[2]
    df          = (pl.from_arrow(table)
                     .filter(pl.col(name_2) >= 0.5)
    )
    index       = df[name_0]
    frequencies = df[name_1]
    pounds      = df[name_2]
    plot_dist(index, pounds)
    plot_freq(index, frequencies)
    print("first_index_at_least_50_percent:\n")
    print(df[-1])

if __name__ == "__main__":
    main()
