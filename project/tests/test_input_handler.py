from src.input_handler import InputHandler
import pytest


@pytest.mark.parametrize(
    "user_input,expected_output",
    [
        ("calgary", "Calgary"),  # Valid input, lowercase
        ("Edmonton", "Edmonton"),  # Valid input, already capitalized
        (" new york ", "New york"),  # Valid input with leading/trailing spaces
    ],
)
def test_get_city_name_valid(mocker, user_input, expected_output):
    """
    Test valid city name inputs.
    Проверяет, что корректные названия городов принимаются.

    :param mocker: A fixture that provides mock functionality.
    :param user_input: Simulated user input for the city name.
    :param expected_output: Expected validated and capitalized city name.
    :assert: The returned city name matches the expected output.
    """
    # Mock the input function to simulate user input
    mocker.patch("builtins.input", return_value=user_input)

    # Call the method and check the result
    assert InputHandler.get_city_name() == expected_output

@pytest.mark.parametrize(
    "user_input,error_message",
    [
        ("abc", "Error: City name must be at least 4 characters long."),  # Too short
        ("1234", "Error: City name must consist of letters, spaces, or hyphens."),  # Invalid characters
        ("!@#$", "Error: City name must consist of letters, spaces, or hyphens."),  # Special characters
    ],
)
def test_get_city_name_invalid(mocker, user_input, error_message):
    """
    Test invalid city name inputs.
    Проверяет, что некорректные названия городов отклоняются.

    :param mocker: A fixture that provides mock functionality.
    :param user_input: Simulated invalid user input for the city name.
    :param error_message: Expected error message for invalid input.
    :param capsys: Pytest fixture to capture printed output.
    :assert: The printed error message matches the expected message.
    """
    # Mock the input function to simulate incorrect input first, then correct
    mock_input = mocker.patch("builtins.input", side_effect=[user_input, "Value City"])

    # Mock the print function to capture the printed output
    mock_print = mocker.patch("builtins.print")

    # Call the method
    InputHandler.get_city_name()

    # Assert that print was called with the expected error message
    mock_print.assert_any_call(error_message)

    # Assert that the method was eventually called 2 times
    assert mock_input.call_count == 2  # (with incorrect data, then with correct data)
