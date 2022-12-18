
import os
import sys
from pathlib import Path


def load_dotenv(*, sep: str = '=') -> None:
    """Загружает данные из ".env" файла и создает на их основе переменные окружения.
    * Файл ".env" должен находиться в одном каталоге с файлом, вызвавшем его.
    * Ключи от значений отделяются знаком "=".
    * Только первый отделитель имеет значение.
    * Убирает лишние пробелы вокруг ключа и значения.

    Example:
    file .env:
    ABC = 123 = 456

    >>> import os
    >>> from dotenv import load_dotenv
    >>> load_dotenv()
    >>> os.getenv('ABC')
    >>> 123 = 456
    """

    # Путь до файла каталога вызвавшего метод
    path = Path(sys.argv[0]).parent / '.env'

    # Если существует ".env" файл по указанному пути
    if path.is_file():
        with open(path) as file:
            for line in file.readlines():
                # Если в строке есть разделитель
                if sep in line:
                    # Делит строку на две части, по первому разделителю
                    line = line.rstrip('\n').split(sep, 1)
                    key, value = [i.strip() for i in line]
                    os.environ[key] = value


if __name__ == '__main__':
    load_dotenv()
    print(os.getenv('ABC'))
