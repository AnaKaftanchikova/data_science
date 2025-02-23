import matplotlib.pyplot as plt
import seaborn as sns

def add_countplot(in_data, x_column = 'Survived', name = 'image'):
    scatter_plot = sns.countplot(x = x_column, data = in_data)
    scatter_fig = scatter_plot.get_figure()
    scatter_fig.savefig(f'out_jpg/{name}.png')

def add_distplot(in_data, x_column = 'Age', name = 'image'):
    scatter_plot = sns.distplot(in_data[x_column])
    scatter_fig = scatter_plot.get_figure()
    scatter_fig.savefig(f'out_jpg/{name}.png')

def add_barplot(in_data, x_column = 'Pclass', y_column = 'Fare', in_hue = 'Survived', name = 'image'):
    scatter_plot = sns.barplot(data = in_data, x = x_column, y = y_column, hue = in_hue)
    scatter_fig = scatter_plot.get_figure()
    scatter_fig.savefig(f'out_jpg/{name}.png')

def add_heatmap(in_data, name = 'image'):
    corr = in_data.corr()
    plt.figure(figsize=(15, 9))
    scatter_plot = sns.heatmap(corr, annot=True, cmap='coolwarm')
    scatter_fig = scatter_plot.get_figure()
    scatter_fig.savefig(f'out_jpg/{name}.png')

