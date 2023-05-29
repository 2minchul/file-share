import uuid

from domain.file_share.dao import LinkRepository
from domain.file_share.dao import model
from domain.file_share.domain.link import Link
from infra.db.sqlite_db import Session


class LinkRepositoryImpl(LinkRepository):
    def crete_link(self, user_id, download_count, file_id) -> Link:
        with Session() as session:
            path = uuid.uuid4().hex.replace('-', '')
            link = model.Link(user_id=user_id, file_id=file_id, path=path, download_count=download_count)
            session.add(link)
            session.commit()
            return Link(
                id=link.id,
                file_id=link.file_id,
                url_path=link.path,
                download_count=link.download_count,
                user_id=link.user_id,
            )

    def get_link_by_path(self, link_path: str) -> Link:
        with Session() as session:
            link = session.query(model.Link).filter(model.Link.path == link_path).first()
            return Link(
                id=link.id,
                file_id=link.file_id,
                url_path=link.path,
                download_count=link.download_count,
                user_id=link.user_id,
            )

    def decrease_download_count(self, link_id: int) -> Link:
        with Session() as session:
            link = session.query(model.Link).filter(model.Link.id == link_id).first()
            link.download_count -= 1
            session.commit()
            return Link(
                id=link.id,
                file_id=link.file_id,
                url_path=link.path,
                download_count=link.download_count,
                user_id=link.user_id,
            )
