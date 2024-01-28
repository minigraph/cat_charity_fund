# YaCut

# FastApi благотворительный проект QRKor
### Описание
Перед Вами проект благотворительного сервиса, реализованный на FastApi. Учебный проект Яндекс.Практикум.
Проект ставит перед собой цели создания и хранения благотворительны проектов и возможности вносить пожертвования на цели проекта.
Использовано:
* Python v.3.9.1 (https://docs.python.org/3.9/)
* fastapi v0.78.0 (https://fastapi.tiangolo.com/)
* SQL Alchemy v1.4.36 (https://docs.sqlalchemy.org/en/14/)
* Alembic v.1.7.7 (https://alembic.sqlalchemy.org/en/latest/)
* Flake 8 v.5.0.4 (https://buildmedia.readthedocs.org/media/pdf/flake8/stable/flake8.pdf)

### Шаблон заполнения .env:
Путь к файлу: 
```
~/.env
```

Ниже представлены примеры заполнения:
* Имя приложения
* Путь и тип базы
* Секретное слово
* Почтовый адрес суперпользователя, создаваемого при первом запуске
* Пароль суперпользователя, создаваемого при первом запуске
```
APP_TITLE=Благотворительный фонд поддержки котиков 
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db 
SECRET=Fortnite
FIRST_SUPERUSER_EMAIL=mail@mail.ru
FIRST_SUPERUSER_PASSWORD=12345qwert
```

### Установка:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/minigraph/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Документация. Примеры запросов:
##### Получение данных всех благотворительных проектов
```
GET http://localhost/charity_project/
```
Ответы:
```
Status code: 200
```
```json
{
  "name": "string",
  "description": "string",
  "full_amount": 0,
  "id": 0,
  "invested_amount": 0,
  "fully_invested": true,
  "create_date": "2024-01-24T14:15:22Z",
  "close_date": "2024-01-24T14:15:22Z"
}
```

##### Запрос на внесения пожертвования 
```
POST http://localhost/donation/
```
Данные:
```json
{
  "full_amount": 0,
  "comment": "string"
}
```
Ответы:
```
Status code: 200
```
```json
{
  "full_amount": 0,
  "comment": "string",
  "id": 0,
  "create_date": "2024-01-24T14:15:22Z"
}
```
```
Status code: 401
```
```json
{
  "detail": "Unauthorized"
}
```

##### Запрос на создание пользователя 
```
POST http://localhost/auth/register/
```
Данные:
```json
{
  "email": "user@example.com",
  "password": "string",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}
```
Ответы:
```
Status code: 201
```
```json
{
  "id": 1,
  "email": "user@example.com",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}
```
```
Status code: 400
```
```json
{
  "detail": "REGISTER_USER_ALREADY_EXISTS"
}
```
```
Status code: 422
```
```json
{
  "detail": 
    [
      {
        "loc": [
            "string"
        ],
        "msg": "string",
        "type": "string"
      }
    ]
}
```

### Автор:
* Михаил Никитин
* * tlg: @minigraf 
* * e-mail: minigraph@yandex.ru;
