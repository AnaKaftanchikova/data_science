import matplotlib.pyplot as plt
import seaborn as sns

def add_line_plot(in_date, x_column = 'cause', y_column = 'cnt_incidents', name = 'bar'):
    plt.figure(figsize=(10, 6))
    plt.bar(in_date[x_column], in_date[y_column])
    plt.title(f'Столбчатая диаграмма для {y_column} по {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    if x_column == 'location':
        plt.xticks(rotation = 90)
    plt.savefig(f'out_jpg/{name}.jpg', bbox_inches='tight')
    plt.show()

def add_plot(in_date, x_column = 'cause', y_column = 'cnt_incidents', name = 'plot'):
    plt.figure(figsize=(10, 6))
    plt.plot(in_date[x_column], in_date[y_column], marker='o')
    plt.title(f'Линейный график для {y_column} по {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.savefig(f'out_jpg/{name}.jpg', bbox_inches='tight')
    plt.show()

def add_lineplot(in_date, x_column = 'cause', y_column = 'cnt_incidents', name = 'lineplot', hue_data = "cause"):
    plt.figure(figsize=(10, 6))
    sns.lineplot(in_date, x = x_column, y = y_column, hue = hue_data)
    plt.title(f'Предполагаемый финансовый ущерб по {x_column}')
    plt.savefig(f'out_jpg/{name}.jpg', bbox_inches='tight')
    plt.show()