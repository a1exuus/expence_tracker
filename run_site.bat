@echo off
REM Переходим в папку с этим батником (корень репозитория)
cd /d "%~dp0"

REM Проверяем, есть ли виртуальное окружение
if not exist "venv\Scripts\activate.bat" (
    echo Создаём виртуальное окружение...
    python -m venv venv
)

REM Активируем виртуальное окружение
call "venv\Scripts\activate.bat"

REM Обновляем pip и ставим зависимости
echo Устанавливаем зависимости...
pip install --upgrade pip
pip install -r requirements.txt

REM Применяем миграции базы данных
echo Применяем миграции...
python manage.py migrate

REM Запускаем сервер и открываем браузер
echo Запускаем сайт...
start http://127.0.0.1:8000
python manage.py runserver

pause
