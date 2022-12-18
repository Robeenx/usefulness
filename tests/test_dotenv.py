
import os
import unittest
from pathlib import Path
from functools import wraps

import get_base_dir
from dotenv import load_dotenv


class TestDotenv(unittest.TestCase):
    """Тестирование переменных окружения"""

    @staticmethod
    def with_env_file(func):
        """Создает .env файл со значениями, для тестирования,
        затем удаляет его."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            path = Path(__file__).parent / '.env'

            # Создание .env файла с тестовым значением
            with open(path, 'w') as file:
                file.write('TEST = 123456789')

            # Устанока локальных переменных из .env файла
            load_dotenv()
            # Тестируемая функция
            func(*args, **kwargs)

            # Удаление .env файла
            if path.is_file():
                os.remove(path)
        return wrapper

    @with_env_file  
    def test_get_enviroments_variable(self):
        """Получение значения из переменной окружения"""
        self.assertEqual(os.getenv('TEST'), '123456789')


if __name__ == '__main__':
    unittest.main()
