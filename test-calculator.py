import calculator
import pytest
from main import get_user_input


def test_addition():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-2, 3) == 1
    assert calculator.add(0, 0) == 0


def test_subtraction():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(3, 5) == -2
    assert calculator.subtract(0, 0) == 0


def test_multiplication():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0, 5) == 0



def test_division():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(10, 2) == 5



def test_division_by_zero():
    try:
        calculator.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."


def test_get_user_input_valid_case1():
    user_input = "2 3"
    expected_values = (2, 3)
    assert get_user_input(user_input) == expected_values

def test_get_user_input_valid_case2():
    user_input = "0 -5"
    expected_values = (0, -5)
    assert get_user_input(user_input) == expected_values

def test_get_user_input_valid_case3():
    user_input = "-10 10"
    expected_values = (-10, 10)
    assert get_user_input(user_input) == expected_values

def test_get_user_input_invalid_case1():
    values_input = "2"
    with pytest.raises(ValueError) as e:
        get_user_input(values_input)
    assert str(e.value) == "Exactly 2 values should be provided."

def test_get_user_input_invalid_case2():
    values_input = "2 3 4"
    with pytest.raises(ValueError) as e:
        get_user_input(values_input)
    assert str(e.value) == "Exactly 2 values should be provided."

def test_get_user_input_invalid_case3():
    values_input = "5"
    with pytest.raises(ValueError) as e:
        get_user_input(values_input)
    assert str(e.value) == "Exactly 2 values should be provided."






#def test_get_user_input_valid():
    # Test valid input values
    test_cases = [
        ("2 3", (2, 3)), 
        ("0 -5", (0, -5)), 
        ("-10 10", (-10, 10)
         )]
    for user_input, expected_values in test_cases:
        assert get_user_input(user_input) == expected_values

#def test_get_user_input_invalid():
    # Test invalid input values (not exactly 2 values provided)
    test_cases = ["2", "2 3 4", "5"]
    for values_input in test_cases:
        with pytest.raises(ValueError) as e:
            get_user_input(values_input)
        assert str(e.value) == "Exactly 2 values should be provided."