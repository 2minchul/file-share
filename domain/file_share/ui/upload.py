from flask.views import MethodView

from common.response import StaticRenderer


class FileShareUploadUIController(MethodView):
    static_renderer: StaticRenderer

    def __init__(self, static_renderer: StaticRenderer):
        self.static_renderer = static_renderer

    def get(self):
        """
        upload file ui
        :return:
        """
        return self.static_renderer.render('upload.html')
