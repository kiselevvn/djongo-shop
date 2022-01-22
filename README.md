# Djongo

Приложение демонстрирует один из возможных вариантов взаимодествия Django и MongoDB

Создание виртуального окружения
```
python3 -m venv .venv
```

Активация виртуального окружения
```
.\.venv\Scripts\activate
```

Установка зависимостей
```
pip install -r .\requirements.txt
```

Выполнение миграций
```
python .\manage.py migrate
```

Создание супер пользователя
```
python .\manage.py createsuperuser
```

Запуск сервера
```
python .\manage.py runserver
```