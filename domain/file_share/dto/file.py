import io
from typing import NamedTuple

from flask import request

from common import DTO


class File(DTO):
    id: int
    name: str
    path: str


class FileUploadRequest(NamedTuple):
    data: bytes
    file_name: str
    download_count: int

    @classmethod
    def parse_from_request(cls) -> 'FileUploadRequest':
        request_file = request.files['file']
        with io.BytesIO() as buffer:
            request_file.save(buffer)
            data = buffer.getvalue()

        return FileUploadRequest(
            data,
            request_file.filename,
            int(request.form['download_count'])
        )


class FileUploadResponse(NamedTuple):
    url: str

    def to_json(self):
        return {
            'url': self.url
        }
