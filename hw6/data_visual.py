import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def add_countplot(in_data, x_column, name = 'image', title = ''):
    plt.figure(figsize=(10, 6))
    if x_column == 'Obesity':
        plt.xticks(rotation = 90)
    plt.title(f"{title}")
    sns_png = sns.countplot(x = x_column, data = in_data, palette='mako')
    for container in sns_png.containers:
        sns_png.bar_label(container)
    scatter_fig = sns_png.get_figure()
    scatter_fig.savefig(f'out_jpg/feature_info/{name}.png')

def add_hist(x_column, name = 'image', title = '', step = 5, max_size = 1):
    bins = np.arange(x_column.min(), x_column.max() + max_size, step)
    plt.figure(figsize=(10, 6))
    plt.title(f"{title}")
    n, bins, patches = plt.hist(x_column, bins=bins, edgecolor='black', alpha=0.7)
    plt.xticks(bins)  
    for count, x in zip(n, bins):
        plt.text(x + (bins[1] - bins[0]) / 2, count, str(int(count)), ha='center', va='bottom')
    plt.savefig(f'out_jpg/feature_info/{name}.png')

def add_heatmap(in_data, name = 'image', title = ''):
    corr = in_data.corr()
    plt.figure(figsize=(15, 9))
    plt.title(f"{title}")
    sns_png = sns.heatmap(corr, annot=True, cmap='coolwarm')
    scatter_fig = sns_png.get_figure()
    scatter_fig.savefig(f'out_jpg/{name}.png')

def add_boxplot(x_column, y_column, name = 'image', title = ''):
    plt.figure(figsize=(10, 6))
    plt.xticks(rotation = 90)
    sns_png = sns.boxplot(x=x_column, y=y_column)
    plt.title(f"{title}")
    scatter_fig = sns_png.get_figure()
    scatter_fig.savefig(f'out_jpg/{name}.png')

'''
def add_scatter(x_column, y_column, anom_column, name = 'image', title = ''):
    plt.figure(figsize=(10, 6))
    sns_png = plt.scatter(x_column, y_column, c=anom_column, cmap='coolwarm', alpha=0.7)
    plt.title(f"{title}")
    plt.xlabel(f"{x_column.name}")
    plt.ylabel(f"{y_column.name}")
    plt.colorbar(label='Аномалия (-1 - аномалия, 1 - нормально)')
    plt.savefig(f'out_jpg/{name}.png')
'''