from common import DTO


class Link(DTO):
    id: int
    user_id: int
    file_id: int
    url_path: str
    download_count: int
