import matplotlib.pyplot as plt
import seaborn as sns

def add_pairplot(in_date, type_hue='cancer_type', type_cancer='lungs', name = 'pairplot'):
    plt.figure(figsize=(10, 6))
    sns.pairplot(in_date[in_date['cancer_type'] == type_cancer], hue=type_hue)
    plt.savefig(f'out_jpg/{name}.jpg', bbox_inches='tight')
    plt.show()

def add_histogram(in_date, column = 'cases', name = 'histogram'):
    plt.hist(in_date[column].dropna())
    plt.title(f'Гистограмма для {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(f'out_jpg/{name}.jpg', bbox_inches='tight')
    plt.show()

def add_line_plot(in_date, x_column = 'location', y_column = 'cases', name = 'line_plot'):
    plt.bar(in_date[x_column], in_date[y_column])
    plt.title(f'Столбчатая диаграмма для {y_column} по {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.savefig(f'out_jpg/{name}.jpg', bbox_inches='tight')
    plt.show()

def add_scatter_plot(in_date, x_column = 'location', y_column = 'cases', name = 'scatter_plot'):
    plt.scatter(in_date[x_column], in_date[y_column])
    plt.title(f'Диаграмма рассеивания для {y_column} по {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.savefig(f'out_jpg/{name}.jpg', bbox_inches='tight')
    plt.show()
