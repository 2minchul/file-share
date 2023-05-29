from flask import Flask

from common.response import LocalStaticRenderer
from domain.file_share.api import FileShareDownloadAPIController, FileShareUploadAPIController
from domain.file_share.application.file_share import FileShareService
from domain.file_share.dao import FileRepository, LinkRepository
from domain.file_share.dao.repository.file import FileRepositoryImpl
from domain.file_share.dao.repository.link import LinkRepositoryImpl
from domain.file_share.ui import FileShareUploadUIController
from domain.file_share.ui.download import FileShareDownloadUIController
from infra.db.sqlite_db import create_tables


class Server(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        create_tables()

        static_renderer = LocalStaticRenderer(self)
        file_repository: FileRepository = FileRepositoryImpl()
        link_repository: LinkRepository = LinkRepositoryImpl()
        file_share_service = FileShareService(file_repository, link_repository)

        self.add_url_rule(
            '/api/file/<string:link_path>',
            view_func=FileShareDownloadAPIController.as_view('file_share_download_api', service=file_share_service),
        )
        self.add_url_rule(
            '/api/file',
            view_func=FileShareUploadAPIController.as_view('file_share_upload_api', service=file_share_service),
        )
        self.add_url_rule(
            '/download/<string:link_path>',
            view_func=FileShareDownloadUIController.as_view('file_share_download_ui', service=file_share_service),
        )
        self.add_url_rule(
            '/',
            view_func=FileShareUploadUIController.as_view('file_share_upload_ui', static_renderer=static_renderer),
        )


app = Server(__name__)

if __name__ == '__main__':
    app.run()
