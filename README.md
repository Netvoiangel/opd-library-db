
# Приложение для сохранения PDF статей 

## Описание

Приложение позволяет пользователям просматривать список статей, добавлять новые статьи, просматривать информацию об авторах и многое другое. В приложении реализована система аутентификации и авторизации пользователей.

## Структура проекта

```
opd-library-db/        # Корневая директория проекта
|-- app/               # Основное приложение Django
|   |-- migrations/    # Миграции БД
|   |-- static/        # Статические файлы (CSS, JavaScript, изображения)
|   |-- templates/     # HTML шаблоны
|   |-- admin.py       # Конфигурация административной панели
|   |-- models.py      # Описание моделей данных
|   |-- urls.py        # Маршруты URL
|   |-- views.py       # Представления
|-- locallibrary/      # Настройки проекта и основные URL
|   |-- settings.py    # Настройки проекта
|   |-- urls.py        # Основные маршруты URL
|   |-- wsgi.py        # Настройки WSGI для развертывания
|-- db.sqlite3         # База данных SQLite
|-- manage.py          # Командная утилита для управления проектом
```

## Модели данных

### Автор (Author)

Модель, представляющая автора статьи.

Поля:
- `user`: Связь с пользователем Django
- `first_name`: Имя автора
- `last_name`: Фамилия автора
- `middle_name`: Отчество автора
- `position`: Должность автора
- `institute`: Институт, к которому принадлежит автор
- `pdf_files`: Статьи, написанные автором

### Статья (PDFFile)

Модель, представляющая статью.

Поля:
- `title`: Название статьи
- `pdf`: PDF файл статьи
- `direction`: Направление статьи
- `authors`: Авторы статьи

## Установка и запуск

1. Склонируйте репозиторий:

```bash
git clone https://github.com/Netvoiangel/opd-library-db.git
```
2. Создайте виртуальную среду Python

```bash
cd opd-library-db
python -m venv venv
source venv/bin/activate # Активация для Mac Os
.\venv\Scripts\activate # Активация на Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите миграции:

```bash
cd app/
python manage.py migrate
```

5. Запустите сервер:

```bash
python manage.py runserver
```

Приложение будет доступно по адресу `http://127.0.0.1:8000/`.

## Тестирование приложения

1. **Создание суперпользователя**:

   Откройте терминал и перейдите в корневую директорию вашего проекта Django. Затем выполните следующую команду:

   ```bash
   python manage.py createsuperuser
   ```

   Следуйте инструкциям в консоли, введите имя пользователя, адрес электронной почты и пароль для создания суперпользователя.

2. **Переход на страницу администратора**:

   Откройте браузер и перейдите по адресу:

   ```
   http://127.0.0.1:8000/admin/
   ```

   Введите имя пользователя и пароль суперпользователя, которые вы создали на предыдущем шаге.

3. **Создание пользователя и автора**:

   На странице администратора найдите раздел "Пользователи" (Users) и нажмите кнопку "Добавить" (Add). Заполните необходимые поля для создания пользователя. После создания пользователя, вернитесь к списку пользователей и выберите Автора (Author). Затем, в меню "Действия" (Actions) выберите "Добавить автора" (Add Author). Это создаст автора на основе пользователя. В поле создания автора заполните данные.

   Теперь у вас есть суперпользователь и автор для тестирования вашего приложения.
