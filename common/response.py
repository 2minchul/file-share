from abc import ABCMeta, abstractmethod

from flask import Response, Flask


class StaticRenderer(metaclass=ABCMeta):
    @abstractmethod
    def render(self, file_path: str) -> Response:
        pass


class LocalStaticRenderer(StaticRenderer):
    app: Flask

    def __init__(self, app: Flask):
        self.app = app

    def render(self, file_path: str) -> Response:
        return self.app.send_static_file(file_path)
