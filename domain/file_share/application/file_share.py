from typing import Tuple

from domain.file_share.dao import FileRepository, LinkRepository


class FileShareService:
    _file_repository: FileRepository
    _link_repository: LinkRepository

    def __init__(self, file_repository: FileRepository, link_repository: LinkRepository):
        self._file_repository = file_repository
        self._link_repository = link_repository

    def download_by_link_path(self, link_path) -> Tuple[str, bytes]:
        """
        download file
        :param link_path:
        :return: (file_name, data)
        """
        link = self._link_repository.get_link_by_path(link_path)
        file = self._file_repository.get_file(link.file_id)
        return file.name, self._file_repository.get_data(file)

    def upload(self, user_id: int, file_name: str, data: bytes, download_count) -> str:
        """
        upload file
        :param user_id:
        :param file_name:
        :param data:
        :param download_count:
        :return: upload link path
        """
        file = self._file_repository.crete_file(file_name, data)
        link = self._link_repository.crete_link(user_id=user_id, download_count=download_count, file_id=file.id)
        return link.url_path

    def get_link_info(self, link_path: str) -> Tuple[str, str]:
        """
        get link info
        :param link_path:
        :return: (file_name, download_count)
        """
        link = self._link_repository.get_link_by_path(link_path)
        file = self._file_repository.get_file(link.file_id)
        return file.name, link.url_path
