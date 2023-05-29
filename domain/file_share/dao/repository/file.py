import os

from domain.file_share.dao import FileRepository
from domain.file_share.dao import model
from domain.file_share.domain.file import File
from infra.db.sqlite_db import Session

_root_path = os.path.join(os.getcwd(), 'files')


class FileRepositoryImpl(FileRepository):

    def crete_file(self, file_name, data: bytes) -> File:
        with open(os.path.join(_root_path, file_name), 'wb') as f:
            f.write(data)

        with Session() as session:
            file = model.File(name=file_name, path=f'files/{file_name}')
            session.add(file)
            session.commit()
            return File(
                id=file.id,
                name=file.name,
                path=file.path,
            )

    def get_file(self, file_id: int) -> File:
        with Session() as session:
            file = session.query(model.File).filter(model.File.id == file_id).first()
            return File(
                id=file.id,
                name=file.name,
                path=file.path,
            )

    def get_data(self, file: File) -> bytes:
        with open(os.path.join(_root_path, file.name), 'rb') as f:
            data = f.read()
        return data
