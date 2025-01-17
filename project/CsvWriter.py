from typing import Iterable
import csv

class CsvWriter:
    @staticmethod
    def write_to_csv(file_path: str, data: Iterable):
        """
        Writes a list of data to a CSV file.
        Записывает список данных в CSV-файл.

        :param file_path: The path to the CSV file.
        :param data: A list of rows to write to the file.
        """
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            for row in data:
                writer.writerow([row])
