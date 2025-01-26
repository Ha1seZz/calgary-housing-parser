from src.DataParser import DataParser
import pytest


# Apply the warning filter globally to all tests in this file
pytestmark = pytest.mark.filterwarnings(
    "ignore:The 'strip_cdata' option of HTMLParser:DeprecationWarning"
)

@pytest.fixture
def html_fragment():
    """Fixture for HTML containing city options."""
    html = """
    <select class="search_fields directorist-location-select">
        <option data-lat="51.0" data-lng="-114.0" data-custom-field="" value="253">Calgary</option>
    </select>
    """
    return html

@pytest.fixture
def html_fragment_with_pages():
    """Fixture for HTML containing pagination with multiple pages."""
    html = """
    <div class="directorist-pagination">
        <a class="page-numbers">2</a>
        <a class="page-numbers">3</a>
        <a class="page-numbers">23</a>
        <a class="page-numbers">""</a>
    </div>
    """
    return html

@pytest.fixture
def html_fragment_with_listings():
    """Fixture for HTML containing multiple address listings."""
    html = """
    <div class="directorist-all-listing-col">
        <div class="directorist-listing-card-address">500 50 Avenue SW, Calgary, Alberta</div>
        <div class="directorist-listing-card-address">120 Na'a Crescent SW Calgary Canada</div>
    </div>
    """
    return html

def test_get_city_options_success(html_fragment):
    """Test successful extraction of city attributes from HTML."""
    city_attrs = DataParser.get_city_options(html_fragment, "Calgary")
    assert city_attrs == {
        "data-lat": "51.0",
        "data-lng": "-114.0",
        "data-custom-field": "",
        "value": "253",
    }

def test_get_city_options_failure(html_fragment):
    """Test failure when the specified city is not found in the HTML."""
    with pytest.raises(ValueError, match="The city 'Calmar' was not found."):
        DataParser.get_city_options(html_fragment, "Calmar")

def test_get_city_options_missing_element():
    """Test failure when the city selection element is missing from the HTML."""
    html = "<div>No select element here</div>"
    with pytest.raises(ValueError, match="The city selection element could not be found."):
        DataParser.get_city_options(html, "Calgary")


def test_get_number_of_pages_single_page():
    """Test that the default number of pages is 1 when pagination is missing."""
    html = "<div>No pagination here</div>"
    num_pages = DataParser.get_number_of_pages(html)
    assert num_pages == 1

def test_get_number_of_pages_success(html_fragment_with_pages):
    """Test successful extraction of the number of pages from pagination HTML."""
    number_of_pages = DataParser.get_number_of_pages(html_fragment_with_pages)
    assert number_of_pages == 23

def test_get_number_of_pages_invalid_structure():
    """Test that the default number of pages is 1 when pagination structure is invalid."""
    html = "<div><a class='page-numbers'>N/A</a></div>"
    num_pages = DataParser.get_number_of_pages(html)
    assert num_pages == 1


def test_extract_addresses_success(html_fragment_with_listings):
    """Test successful extraction of addresses from HTML."""
    listings = DataParser.extract_addresses(html_fragment_with_listings)
    assert listings == ["500 50 Avenue SW, Calgary, Alberta",
                        "120 Na'a Crescent SW Calgary Canada"]

def test_extract_addresses_empty():
    """Test that an empty list is returned when no addresses are found in the HTML."""
    html = "<div>No addresses here</div>"
    addresses = DataParser.extract_addresses(html)
    assert addresses == []
