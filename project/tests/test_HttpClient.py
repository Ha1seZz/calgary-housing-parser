from HttpClient import HttpClient
import pytest


@pytest.fixture
def http_client():
    """Fixture to initialize the HttpClient.
    Used to provide an instance of the HttpClient for the test functions.
    Используется для предоставления экземпляра HttpClient для тестовых функций.

    :return:HttpClient: An instance of the HttpClient class.
    """
    return HttpClient("https://example.com")


def test_get_success(http_client, mocker):
    """Test a successful GET request.
    Simulates a successful GET request by mocking the `requests.Session.get` method.
    Имитирует успешный GET-запрос, имитируя метод `requests.Session.get`.

    :param http_client: The HttpClient instance provided by the fixture.
    :param mocker: A fixture that provides mock functionality.
    :assert: The response from `http_client.get` should match the mocked response text.
    :assert: The `requests.Session.get` method should have been called once with the correct arguments.
    """
    # Mock the response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = "Mock response"

    # Patch the Session.get method
    mock_get = mocker.patch("requests.Session.get", return_value=mock_response)

    # Call the method
    response = http_client.get("https://example.com/test")

    # Assert the response
    assert response == "Mock response"

    # Check if the mocked method was called correctly
    mock_get.assert_called_once_with(
        "https://example.com/test", params=None, timeout=15
    )


def test_get_failure(http_client, mocker):
    """Test a failed GET request.
    Simulates a failed GET request by mocking the `requests.Session.get` method.
    Имитирует неудачный GET-запрос, имитируя метод `requests.Session.get`.

    :param http_client: The HttpClient instance provided by the fixture.
    :param mocker: A fixture that provides mock functionality.
    :assert: The response from `http_client.get` should raise an Exception.
    :assert: The `requests.Session.get` method should have been called once with the correct arguments.
    """
    # Patch the Session.get method to raise an exception
    mock_get = mocker.patch(
        "requests.Session.get", side_effect=Exception("Request failed")
    )

    # Assert that HttpClient.get raises Exception
    with pytest.raises(Exception, match="Request failed"):
        http_client.get("https://example.com/fail")

    # Check if the mocked method was called correctly
    mock_get.assert_called_once_with(
        "https://example.com/fail", params=None, timeout=15
    )
