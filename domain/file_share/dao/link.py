from abc import ABCMeta, abstractmethod

from domain.file_share.domain.link import Link


class LinkRepository(metaclass=ABCMeta):

    @abstractmethod
    def crete_link(self, user_id, download_count, file_id) -> Link:
        pass

    @abstractmethod
    def get_link_by_path(self, link_path: str) -> Link:
        pass

    @abstractmethod
    def decrease_download_count(self, link_id: int) -> Link:
        pass
