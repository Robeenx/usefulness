
import os
import unittest
from pathlib import Path
from functools import wraps

from get_base_dir import *
from dotenv import load_dotenv


# Путь для тестовго .env файла (в тестовом каталоге)
PATH = Path(__file__).parent / '.env'

# Тестовое значение
DATA = {
    'key': 'TEST',
    'val': 'abcd',
}


def env_file_for_tests(func):
    """Создание тестовго .env файла, тестирование
    функции, удаление созданного ранее .env файла"""

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Создание .env файла
        with open(PATH, 'w') as file:
            file.write('='.join(DATA.values()))

        try:
            # Тестируемая функция
            load_dotenv(path=PATH)
            func(*args, **kwargs)
        finally:
            # Удаление .env файла
            if PATH.is_file():
                os.remove(PATH)

    return wrapper


class TestDotenv(unittest.TestCase):
    """Тестирование переменных окружения"""

    @env_file_for_tests
    def test_get_enviroments_variable(self):
        """Получение значения из переменной окружения"""
        self.assertEqual(os.getenv(DATA.get('key')), DATA.get('val'))


if __name__ == '__main__':
    unittest.main()
