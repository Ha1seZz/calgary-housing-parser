from HttpClient import HttpClient
from DataParser import DataParser
from CsvWriter import CsvWriter
from tqdm import tqdm


class Scraper:
    BASE_URL = "https://housingdirectory.ascha.com/"

    def __init__(self, city_name: str):
        """
        Initializes the scraper with the city name and an HTTP client.
        Инициализирует парсер с помощью названия города и HTTP-клиента.

        :param city_name: The name of the city to search.
        """
        self.city_name = city_name
        self.client = HttpClient(self.BASE_URL)

    def run(self):
        """
        Executes the entire scraping process:
        Выполняет весь процесс парсинга:
        - Fetches city options.
        - Finds the number of pages.
        - Extracts addresses.
        - Saves the data to a CSV file.
        """
        print("Fetching city options...")
        html = self.client.get(self.BASE_URL)
        location_attrs = DataParser.get_city_options(html, self.city_name)

        print("Finding number of pages...")
        first_page_url = self.build_search_url(1, location_attrs)
        first_page_html = self.client.get(first_page_url)
        number_of_pages = DataParser.get_number_of_pages(first_page_html)

        print("Extracting addresses...")
        all_addresses = self.address_generator(number_of_pages, location_attrs)

        print("Saving data to CSV...")
        file_path = "data/processed/addresses.csv"
        CsvWriter.write_to_csv(file_path, all_addresses)
        print("Parsing completed. The data is saved to a folder:\n", file_path)

    def address_generator(self, number_of_pages: int, location_attrs: dict):
        """
        Generates addresses page by page.
        Генерирует адреса постранично.

        :param number_of_pages: The total number of pages to parse.
        :param location_attrs: The attributes of the selected city.
        :yield: Addresses from each page.
        """
        for page in tqdm(range(1, number_of_pages + 1), desc="Pages", unit="page"):
            page_url = self.build_search_url(page, location_attrs)
            page_html = self.client.get(page_url)
            for address in DataParser.extract_addresses(page_html):
                yield address

    def build_search_url(self, page, location_attrs: dict) -> str:
        """
        Builds the URL for searching addresses based on city attributes.
        Создает URL-адрес для поиска адресов на основе атрибутов города.

        :param page: The page number to request.
        :param location_attrs: The attributes of the selected city.
        :return: A formatted search URL.
        """
        return (
            f"{self.BASE_URL}search-result/page/{page}/?directory_type=general"
            f"&in_loc={location_attrs['value']}&cityLat={location_attrs['data-lat']}"
            f"&cityLng={location_attrs['data-lng']}&zip&zip-cityLat&zip-cityLng"
            f"&minimum=0&miles=0&q&since"
        )
