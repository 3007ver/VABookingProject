import allure
import pytest
from pydantic import ValidationError
from requests import HTTPError

from core.models.booking import BookingResponse
from conftest import api_client


@allure.feature ("Test create booking")
@allure.suite("Create booking with valid data")
def test_create_booking_with_valid_data(api_client):
    booking_data = {
        "firstname": "Andrew",
        "lastname": "Barry",
        "totalprice": 345,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-06-01",
            "checkout": "2025-06-10"
        },
        "additionalneeds": "Breakfast"
    }
    with allure.step("Create booking with valid data"):
        response = api_client.create_booking(booking_data)
    with allure.step("Verify data in response"):
        try:
            BookingResponse(**response)
        except ValidationError as e:
            raise ValidationError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature ("Test create booking")
@allure.suite("Create booking with valid data from faker")
def test_create_booking_faker_data(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    with allure.step("Create booking with valid data"):
        response = api_client.create_booking(booking_data)
    with allure.step("Verify data in response"):
        try:
            BookingResponse(**response)
        except ValidationError as e:
            raise ValidationError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature("Test create booking")
@allure.suite("Create booking without optional data")
def test_create_booking_without_optional_data(api_client):
    booking_data = {
        "firstname": "Kate",
        "lastname": "Watson",
        "totalprice": 215,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-06-10",
            "checkout": "2025-06-12"
        }
    }
    with allure.step("Create booking without optional data"):
        response = api_client.create_booking(booking_data)
    with allure.step("Verify data in response"):
        try:
            BookingResponse(**response)
        except ValidationError as e:
            raise ValidationError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']

@allure.feature("Test create booking")
@allure.suite("Create booking with invalid data")
def test_create_booking_with_invalid_data(api_client):
    booking_data = {
        "firstname": "",
        "lastname": "Test",
        "totalprice": "not_a_number"
    }
    with allure.step("Verify response code value"):
        with pytest.raises(HTTPError):
            api_client.create_booking(booking_data)






