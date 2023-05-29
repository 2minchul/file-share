from abc import ABCMeta, abstractmethod

from domain.file_share.domain.file import File


class FileRepository(metaclass=ABCMeta):
    @abstractmethod
    def crete_file(self, file_name, data: bytes) -> File:
        pass

    @abstractmethod
    def get_file(self, file_id: int) -> File:
        pass

    @abstractmethod
    def get_data(self, file: File) -> bytes:
        pass
