from bs4 import BeautifulSoup
import requests
import csv


def find_number_of_pages():
    url = f"https://housingdirectory.ascha.com/search-result/?directory_type=general&in_loc=253&cityLat=51.0460954&cityLng=-114.065465&zip=&zip-cityLat=&zip-cityLng=&minimum=0&miles=0&q=&since="
    response = requests.get(url)
    HTML_PAGE = response.text

    soup = BeautifulSoup(HTML_PAGE, "lxml")
    number_pages = int(soup.select("a[class=page-numbers]")[1].get_text()) + 1
    return number_pages

def data_extraction():
    number_pages = find_number_of_pages()
    addresses = []

    for page in range(1, number_pages):
        try:
            url = f"https://housingdirectory.ascha.com/search-result/page/{page}/?directory_type=general&in_loc=253&cityLat=51.0460954&cityLng=-114.065465&zip&zip-cityLat&zip-cityLng&minimum=0&miles=0&q&since#038;in_loc=253&cityLat=51.0460954&cityLng=-114.065465&zip&zip-cityLat&zip-cityLng&minimum=0&miles=0&q&since"
            response = requests.get(url)
        except Exception as e:
            print(f"Error: {e}")
            break

        HTML_PAGE = response.text

        soup = BeautifulSoup(HTML_PAGE, "lxml")

        page_addresses = [address.get_text().strip() for address in soup.find_all("div", class_="directorist-listing-card-address")]
        addresses.extend(page_addresses)

    with open("addresses.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for page_addresses in addresses:
            writer.writerow([page_addresses])

def main():
    data_extraction()

if __name__ == "__main__":
    main()
