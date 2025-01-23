## The purpose of the project:
The code was written for educational purposes
<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Python</title><path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z"/></svg>

# 📄Overview
The [Alberta Seniors Housing Directory](https://housingdirectory.ascha.com/) Parser is a Python-based tool that extracts housing addresses for seniors in Alberta based on a user-provided city name. It fetches data and saves the results into a CSV file.

Libraries used: beautifulsoup4, requests, typing, tqdm

## 🔧️Functions
- Extracts the available cities from the website.
- Checks the names of cities entered by the user.
- Extracts addresses of residential buildings on all pages.
- Saves the extracted data to a CSV file.

## 📜Project Structure

```sh
project/
├── src/
│   ├── HttpClient.py         # Handles HTTP requests with a session.
│   ├── DataParser.py         # Extracts data (city options, addresses, page count) from HTML.
│   ├── CsvWriter.py          # Handles CSV file creation and data writing.
│   ├── Scraper.py            # Orchestrates the scraping process.
│   ├── input_handler.py      # Validates and handles user input.
│   └── main.py               # Entry point of the application.
├── tests/
│   ├── test_HttpClient.py    # Tests for HttpClient class
│   ├── test_DataParser.py    # Tests for DataParser class
│   ├── test_CsvWriter.py     # Tests for CsvWriter class
│   ├── test_Scraper.py       # Tests for Scraper class
│   └── test_input_handler.py # Tests for input handler
├── data/
│   └── processed/            # Contains generated CSV files.
├── requirements.txt          # Python dependencies.
├── .gitignore                # Files and folders to ignore in Git.
├── README.md                 # Project documentation.
└── LICENSE                   # License for the project.
```

## ⚙️Requirements
- ![Python 3.8](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- [Python 3.8 or higher](https://www.python.org/)
- Internet connection
- Installing the necessary dependencies

## 💾Installation
1. Clone the repository:

    ```sh
    git clone https://github.com/Ha1seZz/Alberta-Seniors-Housing-Directory-Parser
    cd Alberta-Seniors-Housing-Directory-Parser
    ```

2. Set Up Virtual Environment (Optional)
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. Install required dependencies:

    ```sh
    python -m pip install -U -r requirements.txt
    ```

## 📝Usage
1. Run the Parser:
   ```sh
   python src/main.py
   ```
2. Follow the instructions:
   - When prompted, enter the name of the city. Make sure that the name matches the name listed in the ASCHA housing directory.
3. Output:
   - Results are saved in data/processed/addresses.csv.
   - Each row in the CSV contains one address.

* * *

## 📃LICENSE
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Ha1seZz/Alberta-Seniors-Housing-Directory-Parser/blob/main/LICENSE) file for details.

## ⚠️Problems
If you have any problems while running the script, you can create a new issue on GitHub or write to Telegram [**@Ha1seZz**](https://t.me/Ha1seZz) with a detailed problem.
