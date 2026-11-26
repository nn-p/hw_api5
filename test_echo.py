import requests
import pytest

BASE_URL = "https://postman-echo.com"


def test_get_with_query_parameters():
    """Тест GET-запроса с query-параметрами."""
    params = {"foo1": "bar1", "foo2": "bar2"}
    response = requests.get(f"{BASE_URL}/get", params=params)

    assert response.status_code == 200, "Статус код должен быть 200"
    data = response.json()
    assert data["args"]["foo1"] == "wrong_value", "Параметр foo1 не совпадает"
    assert data["args"]["foo2"] == "bar2", "Параметр foo2 не совпадает"


def test_post_with_json_body():
    """Тест POST-запроса с JSON-телом."""
    payload = {"name": "test_user", "role": "admin"}
    response = requests.post(f"{BASE_URL}/post", json=payload)

    assert response.status_code == 200, "Статус код должен быть 200"
    data = response.json()
    assert data["json"]["name"] == "test_user", "Имя в JSON не совпадает"
    assert data["json"]["role"] == "admin", "Роль в JSON не совпадает"


def test_post_with_form_data():
    """Тест POST-запроса с данными формы (x-www-form-urlencoded)."""
    payload = {"key1": "value1", "key2": "value2"}
    response = requests.post(f"{BASE_URL}/post", data=payload)

    assert response.status_code == 200, "Статус код должен быть 200"
    data = response.json()
    assert data["form"]["key1"] == "value1", "Данные формы key1 не совпадают"
    assert data["form"]["key2"] == "value2", "Данные формы key2 не совпадают"


def test_get_with_custom_headers():
    """Тест GET-запроса с кастомными заголовками."""
    headers = {"X-My-Custom-Header": "TestValue123"}
    response = requests.get(f"{BASE_URL}/get", headers=headers)

    assert response.status_code == 200, "Статус код должен быть 200"
    data = response.json()
    assert data["headers"]["x-my-custom-header"] == "TestValue123", "Кастомный заголовок не совпадает"


def test_post_reflects_correct_url():
    """Тест проверки того, что сервис корректно возвращает запрошенный URL."""
    payload = {"test": "data"}
    response = requests.post(f"{BASE_URL}/post", json=payload)

    assert response.status_code == 200, "Статус код должен быть 200"
    data = response.json()
    assert data["url"] == f"{BASE_URL}/post", "Возвращенный URL не совпадает с запрошенным"