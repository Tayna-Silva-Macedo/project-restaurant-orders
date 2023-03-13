import csv
from src.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".csv"):
            raise FileNotFoundError(f"Extensão inválida: {file_path}")

        try:
            with open(file_path) as file:
                header = ["customer", "order", "day"]
                reader = csv.DictReader(file, header)
                return list(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {file_path}")
