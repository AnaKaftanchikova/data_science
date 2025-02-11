import pandas as pd

def load_data_csv(file_path):
    """
    Загрузка данных из CSV файла.
    :param file_path: Путь к CSV файлу.
    :return: DataFrame с загруженными данными.
    """
    return pd.read_csv(file_path)

def load_data_json(file_path):
    """
    Загрузка данных из JSON файла.
    :param file_path: Путь к JSON файлу.
    :return: DataFrame с загруженными данными.
    """
    return pd.read_json(file_path)

def load_data_excel(file_path):
    """
    Загрузка данных из Excel файла.
    :param file_path: Путь к Excel файлу.
    :return: DataFrame с загруженными данными.
    """
    return pd.read_excel(file_path)