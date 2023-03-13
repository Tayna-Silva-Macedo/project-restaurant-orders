from abc import ABC, abstractmethod


class Exporter(ABC):
    @classmethod
    @abstractmethod
    def export_data(cls, file_path, data):
        raise NotImplementedError
