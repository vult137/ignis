from wsgiref.simple_server import make_server

from Config import FrameConfig
from DatabaseDescription import DbDescription
from Router import Router


class Application(object):
    def __init__(self, config, host="127.0.0.1", port=8080):
        self.router = config.router
        self.db = config.db
        self.host = host
        self.port = port

    def start_application(self, app):
        with make_server(self.host, self.port, app) as httpd:
            sa = httpd.socket.getsockname()
            print("-----  server established on {0}:{1}  -----".format(self.host, self.port))
            print(sa)
            httpd.serve_forever()


def demo_app(environ, start_response):
    from io import StringIO
    stdout = StringIO()
    h = environ
    print("hello " + environ["PATH_INFO"].strip("/"), file=stdout)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return [stdout.getvalue().encode("utf-8")]


if __name__ == '__main__':
    router = Router()
    db = DbDescription(url="207.246.91.136", port=8080)
    frameConfig = FrameConfig()
    app = Application()
