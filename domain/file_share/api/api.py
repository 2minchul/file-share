from urllib.parse import urlparse

from flask import Response, request, jsonify
from flask.views import MethodView

from domain.file_share.application.file_share import FileShareService
from domain.file_share.dto.file import FileUploadRequest, FileUploadResponse


class FileShareDownloadAPIController(MethodView):
    service: FileShareService

    def __init__(self, service: FileShareService):
        self.service = service

    def get(self, link_path: str):
        """
        download file
        :param link_path:
        :return:
        """
        file_name = data = self.service.download_by_link_path(link_path)
        return Response(
            data,
            mimetype='application/octet-stream',
            headers={'Content-Disposition': f'attachment; filename={file_name}'},
        )


class FileShareUploadAPIController(MethodView):
    service: FileShareService

    def __init__(self, service: FileShareService):
        self.service = service

    def post(self):
        """
        upload file
        :return:
        """
        params = FileUploadRequest.parse_from_request()
        request_url = urlparse(request.base_url)
        # TODO: add user
        link_path = self.service.upload(0, params.file_name, params.data, params.download_count)
        url = f'{request_url.scheme}://{request_url.netloc}/download/{link_path}'
        return jsonify(FileUploadResponse(url).to_json())
