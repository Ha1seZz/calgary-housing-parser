from src.DataParser import DataParser
import pytest


# Apply the warning filter globally to all tests in this file
pytestmark = pytest.mark.filterwarnings(
    "ignore:The 'strip_cdata' option of HTMLParser:DeprecationWarning"
)

@pytest.fixture
def html_fragment():
    """Fixture for HTML containing city options.
    Фикстура для HTML, содержащего опции города.

    :return: A string with HTML containing a select element with city options.
    """
    html = """
    <select class="search_fields directorist-location-select">
        <option data-lat="51.0" data-lng="-114.0" data-custom-field="" value="253">Calgary</option>
    </select>
    """
    return html

@pytest.fixture
def html_fragment_with_pages():
    """Fixture for HTML containing pagination with multiple pages.
    Фикстура для HTML, содержащего пагинацию с несколькими страницами.

    :return: A string with HTML containing pagination elements.
    """
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
    """Fixture for HTML containing multiple address listings.
    Фикстура для HTML, содержащего несколько адресов.

    :return: A string with HTML containing address elements.
    """
    html = """
    <div class="directorist-all-listing-col">
        <div class="directorist-listing-card-address">500 50 Avenue SW, Calgary, Alberta</div>
        <div class="directorist-listing-card-address">120 Na'a Crescent SW Calgary Canada</div>
    </div>
    """
    return html

def test_get_city_options_success(html_fragment):
    """Test a successful extraction of city attributes from HTML.
    Тест успешного извлечения атрибутов города из HTML.

    :param html_fragment: Fixture containing the HTML with city options.
    :assert: The returned dictionary matches the expected attributes for "Calgary".
    """
    city_attrs = DataParser.get_city_options(html_fragment, "Calgary")
    assert city_attrs == {
        "data-lat": "51.0",
        "data-lng": "-114.0",
        "data-custom-field": "",
        "value": "253",
    }

def test_get_city_options_failure(html_fragment):
    """Test a failure case when the specified city is not found in the HTML.
    Тест на случай ошибки, когда указанный город не найден в HTML.

    :param html_fragment: Fixture containing the HTML with city options.
    :assert: A ValueError is raised with the appropriate message.
    """
    with pytest.raises(ValueError, match="The city 'Calmar' was not found."):
        DataParser.get_city_options(html_fragment, "Calmar")

def test_get_city_options_missing_element():
    """Test a failure case when the city selection element is missing from the HTML.
    Тест на случай ошибки, когда элемент выбора города отсутствует в HTML.

    :assert: A ValueError is raised with the appropriate message.
    """
    html = "<div>No select element here</div>"
    with pytest.raises(ValueError, match="The city selection element could not be found."):
        DataParser.get_city_options(html, "Calgary")


def test_get_number_of_pages_single_page():
    """Test the default number of pages is 1 when pagination is missing.
    Тест на случай, если по умолчанию количество страниц равно 1 при отсутствии пагинации.

    :assert: The returned number of pages is 1.
    """
    html = "<div>No pagination here</div>"
    num_pages = DataParser.get_number_of_pages(html)
    assert num_pages == 1

def test_get_number_of_pages_success(html_fragment_with_pages):
    """Test a successful extraction of the number of pages from pagination HTML.
    Тест успешного извлечения количества страниц из HTML пагинации.

    :param html_fragment_with_pages: Fixture containing HTML with pagination elements.
    :assert: The number of pages matches the expected value.
    """
    number_of_pages = DataParser.get_number_of_pages(html_fragment_with_pages)
    assert number_of_pages == 23

def test_get_number_of_pages_invalid_structure():
    """Test the default number of pages is 1 when pagination structure is invalid.
    Тест на случай, если по умолчанию количество страниц равно 1 при некорректной структуре пагинации.

    :assert: The returned number of pages is 1.
    """
    html = "<div><a class='page-numbers'>N/A</a></div>"
    num_pages = DataParser.get_number_of_pages(html)
    assert num_pages == 1


def test_extract_addresses_success(html_fragment_with_listings):
    """Test a successful extraction of addresses from HTML.
    Тест успешного извлечения адресов из HTML.

    :param html_fragment_with_listings: Fixture containing HTML with address listings.
    :assert: The list of extracted addresses matches the expected result.
    """
    listings = DataParser.extract_addresses(html_fragment_with_listings)
    assert listings == ["500 50 Avenue SW, Calgary, Alberta",
                        "120 Na'a Crescent SW Calgary Canada"]

def test_extract_addresses_empty():
    """Test that an empty list is returned when no addresses are found in the HTML.
    Тест на случай, если возвращается пустой список, когда в HTML нет адресов.

    :assert: The returned list is empty.
    """
    html = "<div>No addresses here</div>"
    addresses = DataParser.extract_addresses(html)
    assert addresses == []
