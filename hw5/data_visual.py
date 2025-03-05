import matplotlib.pyplot as plt
import seaborn as sns

def add_barh(x_column, y_column, name = 'image'):
    plt.figure(figsize=(10,8))
    plt.barh(x_column, y_column)
    plt.xlabel('Importance')
    plt.title(f"{name}")
    plt.savefig(f'out_jpg/{name}.png')

def add_result_predict(x_column, y_test, y_pred, name = 'image'):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_column, y_test, color='blue', label='Фактические значения')
    plt.scatter(x_column, y_pred, color='red', label='Предсказанные значения')
    plt.xlabel('Наблюдение')
    plt.ylabel('Значение')
    plt.title(f"Фактические и предсказанные значения по регрессору {name}")
    plt.legend()
    plt.savefig(f'out_jpg/{name}.png')