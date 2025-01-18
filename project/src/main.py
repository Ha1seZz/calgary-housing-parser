from input_handler import InputHandler
from Scraper import Scraper

def main():
    """
    Main entry point for the program.
    Основная точка входа в программу.
    
    Initializes input handling and starts the scraper.
    """
    print("Starting Alberta Seniors Housing Directory Parser...")
    city_name = InputHandler.get_city_name()
    scraper = Scraper(city_name)
    scraper.run()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
