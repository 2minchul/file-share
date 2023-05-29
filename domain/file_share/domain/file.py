from dataclasses import dataclass

from common import Entity


@dataclass
class File(Entity):
    id: int
    name: str
    path: str
