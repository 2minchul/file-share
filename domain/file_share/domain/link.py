from dataclasses import dataclass

from common import Entity


@dataclass
class Link(Entity):
    id: int
    user_id: int
    file_id: int
    url_path: str
    download_count: int
