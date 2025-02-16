import sqlite3
import pandas as pd
import log

class SQLiteDB:
    def __init__(self, db_name):
        try:
            log.add_log_info('Инициализация подключения к базе данных')
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            log.add_log_info(f"Подключено к базе данных: {db_name}")
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")
        finally:
            log.add_log_debug('finally_after_init')
    
    def create_table(self, table_name, columns):
        try:
            log.add_log_info('Создание таблицы в базе данных')
            columns_detail = ', '.join([f"{col} {typ}" for col, typ in columns.items()])
            sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_detail});"
            self.cursor.execute(sql)
            self.connection.commit()
            log.add_log_info(f"Таблица {table_name} создана или уже существует.")
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")
        finally:
            log.add_log_debug('finally_after_create_table')
            
    def insert_data_placeholder(self, table_name, data):
        try:
            log.add_log_info('Вставка данных в таблицу используя placeholder')
            placeholders = ', '.join(['?' for _ in data])
            sql = f"INSERT INTO {table_name} VALUES ({placeholders});"
            self.cursor.execute(sql, data)
            self.connection.commit()
            log.add_log_info('Данные вставлены успешно')
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")
        finally:
            log.add_log_debug('finally_after_insert_data')

    def insert_data_many(self, table_name, columns_insert, columns_values_insert, data):
        try:
            log.add_log_info('Вставка данных в таблицу через executemany')
            insert_records = f"INSERT INTO {table_name} ({columns_insert}) VALUES ({columns_values_insert});"
            self.cursor.executemany(insert_records, data)
            self.connection.commit()
            log.add_log_info('Данные вставлены успешно')
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")
        finally:
            log.add_log_debug('finally_after_insert_data')
            
    def fetch_all(self, table_name):
        try:
            log.add_log_info('Получение всех данных из таблицы')
            sql = f"SELECT * FROM {table_name};"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")
        else:
            return results
        finally:
            log.add_log_debug('finally_after_fetch_all')

    def fetch_data_with_query(self, query):
        try:
            log.add_log_info('Получение данных из таблицы по условию')
            sql = f"{query};"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")
        else:
            return results
        finally:
            log.add_log_debug('finally_after_fetch_data_with_query')

    def prepare_data(self, query):
        try:        
            data = pd.read_sql_query(query, self.connection)
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")    
        else:
            return data
        finally:
            log.add_log_debug('finally_after_prepare_data')

    def delete_data(self, query):
        try:
            log.add_log_info('Удаление данных из таблицы по условию')
            sql = f"{query};"
            self.cursor.execute(sql)
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")
        finally:
            log.add_log_debug('finally_after_fetch_data_with_query')

    def close(self):
        try:
            log.add_log_info('Закрытие соединения с базой данных')
            self.connection.close()
            log.add_log_info('Соединение с базой данных закрыто')
        except Exception as e:
            log.add_log_error(f"Произошла ошибка: {e}")
        finally:
            log.add_log_debug('finally_after_close')