from src.exporter.exporter import Exporter


class TxtExporter(Exporter):
    @classmethod
    def export_data(cls, file_path, data):
        file = open(file_path, "w")

        for item in data:
            file.write(f"{item}\n")

        file.close()
