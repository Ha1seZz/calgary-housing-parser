## The purpose of the project:
The code was written for educational purposes

# Overview
The [Alberta Seniors Housing Directory](https://housingdirectory.ascha.com/) Parser is a Python-based tool that extracts housing addresses for seniors in Alberta based on a user-provided city name. It fetches data and saves the results into a CSV file.

Libraries used: beautifulsoup4, requests, typing

## Functions
- Extracts the available cities from the website.
- Checks the names of cities entered by the user.
- Extracts addresses of residential buildings on all pages.
- Saves the extracted data to a CSV file.

## Project Structure

```sh
project/
├── src/
│   ├── HttpClient.py       # Handles HTTP requests with a session.
│   ├── DataParser.py       # Extracts data (city options, addresses, page count) from HTML.
│   ├── CsvWriter.py        # Handles CSV file creation and data writing.
│   ├── Scraper.py          # Orchestrates the scraping process.
│   ├── input_handler.py    # Validates and handles user input.
│   └── main.py             # Entry point of the application.
├── tests/                  # Unit tests for each module.
│   ├── Soon...
├── data/                   # Directory for processed output.
│   └── processed/          # Contains generated CSV files.
├── requirements.txt        # Python dependencies.
├── .gitignore              # Files and folders to ignore in Git.
├── README.md               # Project documentation.
└── LICENSE                 # License for the project.
```

## Requirements
- [Python 3.8 or higher](https://www.python.org/)
- Internet connection

## Installation
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

## Usage
1. Run the Parser:
   ```sh
   python src/main.py
   ```
2. Follow the instructions:
   - When prompted, enter the name of the city. Make sure that the name matches the name listed in the ASCHA housing directory.
3. Output:
   - Results are saved in data/processed/addresses.csv.
   - Each row in the CSV contains one address.
