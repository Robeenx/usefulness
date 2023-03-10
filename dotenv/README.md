# Создание переменных окружения

###### _Что делает метод:_ 
```
Загружает данные из ".env" файла и создает на их основе переменные окружения.
```

###### _Особенности:_
```
Файл ".env" должен находиться в одном каталоге с файлом вызвавшем его.
Ключи от значений отделяются знаком "=".
Только первый отделитель имеет значение.
Убирает лишние пробелы вокруг ключа и значения.
```

###### _Пример использования:_
```
Файл ".env":
ABC = 123 = 456
```

```
>>> import os
>>> from usefulness import dotenv
>>>
>>> dotenv.load_dotenv()
>>> os.getenv('ABC')
>>> 123 = 456
```