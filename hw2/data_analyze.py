import pandas as pd

def check_data(in_data):
    """
    Проверка на пропуски.
    :param in_data: входящий DataFrame.
    :return: проверенный DataFrame.
    """
    return pd.isnull(in_data)

def set_missing_values(in_data, column, method='mode'):
    """
    В зависимости от метода исключение пропук.
    :param 
        in_data: входящий DataFrame;
        column: заполняемый столбец.
    :return: измененный DataFrame.
    """
    if column.name in in_data.columns:
        if method == 'mean':
            return in_data.fillna(column.mean())
        elif method == 'median':
            return in_data.fillna(column.median())
        elif method == 'delete':
            return in_data.dropna()
        else:
            raise ValueError("Метод должен быть 'mean', 'median', or 'delete'")
    else:
        raise ValueError("Столбец не найден")