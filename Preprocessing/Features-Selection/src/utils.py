import numpy as np
import matplotlib.pyplot as plt


def plot_bar_feature(
    freq_feature: dict[str, int], title: str, figsize: tuple[int, int] = (10, 6)
):
    height = np.array(list(dict(freq_feature).values()))
    plt.figure(figsize=figsize)
    plt.bar(x=range(0, len(freq_feature)), height=height)
    plt.xticks(
        ticks=range(0, len(freq_feature)), labels=list(freq_feature.keys()), rotation=80
    )
    plt.title(title)
    plt.show()
