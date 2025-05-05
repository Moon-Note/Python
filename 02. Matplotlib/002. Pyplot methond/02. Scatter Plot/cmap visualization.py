import matplotlib.pyplot as plt
import numpy as np

# 색상 맵 목록
cmap_names = [
    'viridis', 'plasma', 'inferno', 'magma', 'cividis',  # Perceptually Uniform Sequential
    'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',  # Sequential
    'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',  # Sequential continued
    'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',  # Sequential continued
    'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',  # Diverging
    'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',  # Diverging continued
    'twilight', 'twilight_shifted', 'hsv',  # Cyclic
    'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',  # Qualitative
    'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c',  # Qualitative continued
    'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',  # Miscellaneous
    'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',  # Miscellaneous continued
    'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'  # Miscellaneous continued
]

# 색상 맵 시각화 함수
def plot_color_gradients(cmap_list):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    fig, axes = plt.subplots(nrows=len(cmap_list), figsize=(8, 0.3 * len(cmap_list)))
    fig.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10, transform=ax.transAxes)
        ax.set_axis_off()

    plt.show()

# 선택한 색상 맵 목록 시각화
plot_color_gradients(cmap_names)
