import re


class InputHandler:
    @staticmethod
    def get_city_name():
        """
        Requests and validates the city name from the user.
        Запрашивает и проверяет название города у пользователя.

        :return: A validated city name (capitalized).
        """
        while True:
            city = input("Enter the city: ").strip()
            if len(city) < 4:
                print("Error: City name must be at least 4 characters long.")
            elif not re.match(r"^[a-zA-Z\s-]+$", city):
                print("Error: City name must consist of letters, spaces, or hyphens.")
            else:
                return city.capitalize()
