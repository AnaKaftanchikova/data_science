import log
import csv

def open_file(file_path):
    try:
        file = open(file_path, encoding="utf-8")
        contents = csv.reader(file)
        log.add_log_info('Чтение файла прошло успешно')
    except FileNotFoundError:
        log.add_log_error('Файл не найден')
    except Exception as e:
        log.add_log_error(f"Произошла ошибка: {e}")
    else:
        return contents
    finally:
        log.add_log_debug('finally_after_open_csv')