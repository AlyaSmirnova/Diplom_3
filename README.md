# 3-я часть дипломной работы: автоматизированное UI-тестирование для сайта [StellarBurgers](https://stellarburgers.nomoreparties.site).

В проекте описаны автоматизированные UI-тесты для сайта StellarBurgers, реализованные с использованием **Selenium Webdriver**, **pytest**, **Allure** и **Page Object Model**.

Были протестированы: 
- страница восстановления пароля;
- личный кабинет;
- основной функционал сайта; 
- раздел "Лента заказов".

## Технологии
- Python 3.10+
- [pytest](https://docs.pytest.org/)
- [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)
- [Allure](https://docs.qameta.io/allure/)
- [Google Chrome](https://www.google.com/intl/ru_ru/chrome/) / [Firefox](https://www.mozilla.org/ru/firefox/new/)

## Структура проекта
```text
Diplom_2/
    ├── pages                    # Page Object модели страниц
    │   ├── base_page.py       
    │   ├── main_page.py
    │   ├── login_page.py
    │   ├── personal_account_page.py
    │   ├── reset_password_page.py
    │   ├── order_queue_page.py
    │  
    ├── srs/                   # Вспомогательные модули
    │   ├── config.py      
    │   ├── data.py
    │   ├── locators.py
    │ 
    ├── tests/                 # Тестовые сценарии
    │   ├── test_reset_password_page.py
    │   ├── test_personal_account_page.py
    │   ├── test_main-functionality_page.py
    │   ├── test_order_queue_page.py
    │   
    ├── conftest.py              # Файл с фикстурами
    ├── pytest.ini               # Конфигурационный файл
    ├── requirements.txt         # Файл с зависимостями для проекта
    └── allure-resullts           # Allure-отчет
```

## Быстрый старт 
1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/AlyaSmirnova/Diplom_3
cd Diplom_3
```

2. **Создайте и активируйте виртуальное окружение:**
```bash
python -m venv venv
source venv/bin/activate       # для Linux/MacOS
venv\Scripts\activates         # для Windows
```

3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

4. **Установите Allure (если не установлен):**
```bash
- MacOS: brew install allure
- Windows: choco install allure
```

5. **Запуск тестов:**
```bash
- Chrome: pytest --browser_name=chrome
- Firefox: pytest --browser_name=firefox
```

6. **Генерация и просмотр Allure-отчёта:**
```bash
pytest --alluredir=allure-results
allure serve allure-results 
```

