from parser import data_extraction

def main():
    print("Starting Calgary Housing Parser...")
    data_extraction()
    print("Parsing completed. Data saved to 'data/processed/addresses.csv'.")

if __name__ == "__main__":
    main()
