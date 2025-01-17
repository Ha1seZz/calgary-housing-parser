from bs4 import BeautifulSoup


class DataParser:
    @staticmethod
    def get_city_options(html: str, city_name: str) -> dict:
        """
        Searches for city attributes by name in the given HTML.
        Выполняет поиск атрибутов города по названию в заданном HTML-коде.

        :param html: The HTML content to search within.
        :param city_name: The name of the city to find.
        :return: A dictionary of the city's attributes.
        :raises ValueError: If the city selection element or the city is not found.
        """
        soup = BeautifulSoup(html, "lxml")
        location_tag = soup.select_one(
            "select[class='search_fields directorist-location-select']"
        )
        if not location_tag:
            raise ValueError("The city selection element could not be found.")

        option = location_tag.find("option", string=city_name)
        if not option:
            raise ValueError(f"The city '{city_name}' was not found.")
        return option.attrs

    @staticmethod
    def get_number_of_pages(html: str) -> int:
        """
        Extracts the number of pages available for parsing.
        Извлекает количество страниц, доступных для анализа.

        :param html: The HTML content of a search results page.
        :return: The number of pages (default is 1 if not found).
        """
        soup = BeautifulSoup(html, "lxml")
        try:
            page_numbers = soup.select("a.page-numbers")
            return int(page_numbers[-2].get_text()) if page_numbers else 1
        except (IndexError, ValueError):
            return 1

    @staticmethod
    def extract_addresses(html: str):
        """
        Extracts all addresses from the given HTML content.
        Извлекает все адреса из заданного HTML-содержимого.

        :param html: The HTML content of a search results page.
        :return: A list of extracted addresses.
        """
        soup = BeautifulSoup(html, "lxml")
        return [
            address.get_text().strip()
            for address in soup.find_all(
                "div", class_="directorist-listing-card-address"
            )
        ]
