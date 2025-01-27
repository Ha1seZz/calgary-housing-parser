from HttpClient import HttpClient
from DataParser import DataParser
from CsvWriter import CsvWriter
from Scraper import Scraper
import pytest


@pytest.fixture
def scraper():
    """Fixture to provide a Scraper instance for tests."""
    return Scraper(city_name="Calgary")

@pytest.fixture
def mock_http_client(mocker):
    """Fixture to mock the HttpClient class used in the Scraper."""
    return mocker.patch("Scraper.HttpClient", autospec=True)

@pytest.fixture
def mock_data_parser(mocker):
    """Fixture to mock the DataParser class used in the Scraper."""
    return mocker.patch("Scraper.DataParser", autospec=True)

@pytest.fixture
def mock_csv_writer(mocker):
    """Fixture to mock the CsvWriter class used in the Scraper."""
    return mocker.patch("Scraper.CsvWriter", autospec=True)

def test_scraper_initialization(scraper):
    """Test the correct initialization of the Scraper instance.
    Тест корректной инициализации экземпляра Scraper.

    :param scraper: Fixture providing the Scraper instance.
    :assert: The city_name is correctly assigned, and the client is an instance of HttpClient.
    """
    assert scraper.city_name == "Calgary"
    assert isinstance(scraper.client, HttpClient)


def test_build_search_url(scraper):
    """Test the correct construction of the search URL.
    Тест корректного создания URL-адреса для поиска.

    :param scraper: Fixture providing the Scraper instance.
    :assert: The generated URL matches the expected format based on location attributes and page number.
    """
    location_attrs = {
        "data-lat": "51.0460954",
        "data-lng": "-114.065465",
        "data-custom-field": "",
        "value": "253",
    }
    url = scraper.build_search_url(2, location_attrs)
    expected_url = (
        "https://housingdirectory.ascha.com/search-result/page/2/?directory_type=general"
        "&in_loc=253&cityLat=51.0460954&cityLng=-114.065465&zip&zip-cityLat&zip-cityLng"
        "&minimum=0&miles=0&q&since"
    )
    assert url == expected_url


def test_address_generator(scraper, mock_http_client, mock_data_parser, mocker):
    """Test the address generation process page by page.
    Тест процесса генерации адресов постранично.

    :param scraper: Fixture providing the Scraper instance.
    :param mock_http_client: Mocked HttpClient instance.
    :param mock_data_parser: Mocked DataParser instance.
    :param mocker: Pytest-mock object for applying patches.
    :assert: The correct number of HTTP client calls and address parsing calls are made,
            and the resulting addresses match the expected output.
    """
    mocker.patch.object(scraper, "client", mock_http_client)
    mock_http_client.get.return_value = "<html>mocked_html</html>"
    mock_data_parser.extract_addresses.return_value = ["Address 1", "Address 2"]

    location_attrs = {"data-lat": "51.0460954", "data-lng": "-114.065465",
                      "data-custom-field": "", "value": "253"}

    addresses = list(scraper.address_generator(2, location_attrs))

    assert mock_http_client.get.call_count == 2, f"Expected 2 calls, got {mock_http_client.get.call_count}"
    assert mock_data_parser.extract_addresses.call_count == 2, f"Expected 2 calls, got {mock_data_parser.extract_addresses.call_count}"
    assert addresses == ["Address 1", "Address 2", "Address 1", "Address 2"], f"Unexpected addresses: {addresses}"
