# VABookingProject — API Autotests (Python + pytest)

Автоматизированные API-тесты для сервиса бронирования [Restful-Booker](https://restful-booker.herokuapp.com).

Реализован паттерн **API Client** (аналог Page Object для API): логика запросов вынесена в отдельный клиентский слой, тесты работают только с бизнес-логикой.

---

## Стек

| Инструмент | Назначение |
|---|---|
| Python 3.11+ | Язык разработки |
| pytest | Фреймворк для тестов |
| requests | HTTP-клиент |
| Faker | Генерация тестовых данных |
| Pydantic | Валидация схемы ответов |
| python-dotenv | Управление переменными окружения |
| Allure | Отчётность |

---

## Структура проекта

```
VABookingProject/
├── core/
│   └── clients/
│       └── api_client.py   # API-клиент (все HTTP-запросы)
├── tests/                  # Тест-кейсы (CRUD, авторизация, негативные)
├── conftest.py             # Фикстуры: api_client (session), тестовые данные (Faker)
├── pytest.ini              # Конфигурация pytest + Allure
├── requirements.txt        # Зависимости
├── .env.example            # Пример переменных окружения
└── .gitignore
```

---

## Что покрывают тесты

- Создание бронирования (POST /booking)
- Получение бронирования по ID (GET /booking/:id)
- Обновление бронирования (PUT/PATCH /booking/:id)
- Удаление бронирования (DELETE /booking/:id)
- Валидация схемы ответа (Pydantic)
- Негативные сценарии (неверный токен, несуществующий ID)

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/3007ver/VABookingProject.git
cd VABookingProject
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Создать файл `.env`

```bash
cp .env.example .env
```

Переменные уже заполнены дефолтными значениями для публичного API — менять не нужно.

### 4. Запустить тесты

```bash
# Все тесты
pytest

# С подробным выводом
pytest -v

# Конкретная группа тестов
pytest tests/test_create_booking.py -v
```

### 5. Открыть Allure-отчёт

```bash
allure serve allure-results
```

---

## CI

Тесты автоматически запускаются при каждом пуше и pull request через **GitHub Actions**.  
Результаты доступны во вкладке [Actions](../../actions).
