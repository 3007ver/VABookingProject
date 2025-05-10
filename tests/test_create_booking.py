import pytest
import allure
import requests

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
        assert "bookingid" in response
        assert response["booking"] == booking_data

@allure.feature ("Test create booking")
@allure.suite("Create booking with valid data from faker")
def test_create_booking_faker_data(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    with allure.step("Create booking with valid data"):
        response = api_client.create_booking(booking_data)
    with allure.step("Verify data in response"):
        assert "bookingid" in response
        assert response["booking"] == booking_data
