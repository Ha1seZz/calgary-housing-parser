from src.CsvWriter import CsvWriter
import pytest


@pytest.fixture
def sample_data():
    """Fixture providing sample data to be written to a CSV file.
    Фикстура, предоставляющая пример данных для записи в CSV-файл.

    :return: A list of strings representing rows.
    """
    return ["Row 1", "Row 2", "Row 3"]

@pytest.fixture
def temp_file(tmp_path):
    """Fixture providing a temporary file path for testing.
    Фикстура, предоставляющая временный путь к файлу для тестирования.

    :param tmp_path: A built-in pytest fixture for creating temporary directories.
    :return: The path to a temporary file.
    """
    return tmp_path / "test_output.csv"

def test_write_to_csv_success(temp_file, sample_data):
    """Test successful writing of data to a CSV file.
    Тест успешной записи данных в CSV-файл.

    :param temp_file: The temporary file path provided by the fixture.
    :param sample_data: The sample data to write to the file.
    :assert: The file contains the expected data written in CSV format.
    """
    # Write data to the file
    CsvWriter.write_to_csv(temp_file, sample_data)

    # Verify the file contents
    with open(temp_file, "r") as file:
        content = file.read().splitlines()
    assert content == ["Row 1", "Row 2", "Row 3"]
