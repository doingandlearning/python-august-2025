from maths import add
import pytest
from pytest import approx


def setup_function():
    print("Runs before each test")

def teardown_function():
    print("Runs after each test")


@pytest.fixture()
def setup_and_teardown():
    print("Setting up for this test")
    mock = "THISISAMOCK"
    yield  # handing control to the test
    print("Tearing down this test")

def test_adding_two_whole_numbers(setup_and_teardown):
    print(f"Inside the testfunction: {setup_and_teardown}")
    # Arrange - Given
    a = 10
    b = 12
    # Act - When
    result = add(10, 12)
    # Assert - Then
    assert result == 22
    assert add(10, 12) == 22


@pytest.mark.skip("Not implemented yet.")
def test_adding_zero_does_not_change_value():
    result = add(10, 0)
    assert result == 10


# decorators!  annotations.
@pytest.mark.parametrize(
    "a, b, expected_result", [
        (1, 1, 2),
        (-1, -1, -2),
        (1.1, 2.2, 3.3),
        (-1_000_000, 1_000_000, 0),
        (10, 11, 21)

    ]
)
def test_adding_numbers_returns_valid_result(setup_and_teardown, a, b, expected_result):
    print(setup_and_teardown)
    result = add(a, b)
    assert result == approx(expected_result)

# parameterizing tests
# skipping
# testing unhappy paths - getting errors!

def test_raises_error_when_trying_to_add_strings():
    with pytest.raises(TypeError):
        add("1", "seven")

import requests
def test_api_response():
    response = requests.get("https://swapi.dev/api/people/1")
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data["name"] == "Luke Skywalker"