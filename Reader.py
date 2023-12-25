import csv
import os
from collections import namedtuple


class Reader:
    """ Класс чтения файлов """
    DATA_FROM_FILE = namedtuple("Data", ["head", "body"])

    @classmethod
    def read_csv_file(cls, file: str, delimiter: str) -> namedtuple:
        """ Функция чтения csv файлов и деления его на head и body, где head - имена полей столбцов,
        а body - строки данных """
        file = cls.find_file(name=file)
        # Формирование пустого списка для внесения в него данных из считанных строк
        test_data = []
        # Открытие файла при помощи контекстного менеджера
        with open(file, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=delimiter)
        # Формирование переменной с именами полей файла в виде строки
        head = next(data)
        # Добавление в список всех считанных строк файла
        for row in data:
            test_data.append(row)
        # Возврат именованного кортежа с head в виде имен столбцов, а body в виде строк данных
        return cls.DATA_FROM_FILE(','.join(head), test_data)

    @staticmethod
    def find_file(name: str) -> str:
        """ Функция поиска файла по введенному имени во всех вложенных в проект папках """
        for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
            if name in files:
                return os.path.join(root, name)
