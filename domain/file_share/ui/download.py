from urllib.parse import urlparse

from flask import render_template, request
from flask.views import MethodView

from domain.file_share.application.file_share import FileShareService


class FileShareDownloadUIController(MethodView):
    service: FileShareService

    def __init__(self, service: FileShareService):
        self.service = service

    def get(self, link_path: str):
        """
        download file ui
        :param link_path:
        :return:
        """
        file_name, link_path = self.service.get_link_info(link_path)
        request_url = urlparse(request.base_url)
        download_url = f'{request_url.scheme}://{request_url.netloc}/download/{link_path}'

        return render_template('download.html', file_name=file_name, download_url=download_url)
