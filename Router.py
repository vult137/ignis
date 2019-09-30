class RouterItem(object):
    def __init__(self, url, view_func):
        self.url = url
        self.view_func = view_func


class Router(object):
    def __init__(self):
        self.router_table = []

    def register(self, **kwargs):
        item = kwargs.get("item")
        if item is not None and type(item) == RouterItem:
            self.router_table.append(item)
            return

        url = kwargs.get("url")
        view_func = kwargs.get("view_func")
        if url is not None and view_func is not None:
            item = RouterItem(url, view_func)
            return

    def remove(self, url):
        for item in self.router_table:
            if item.url == url:
                self.router_table.remove(item)
                break

    def registerFromDict(self, router_dict):
        for item in router_dict:
            try:
                self.register(item=item)
            except ValueError as ve:
                pass

    def clearTable(self):
        self.router_table = []

    def getViewfuncOrNone(self, url):
        for item in self.router_table:
            if item.url == url:
                return item.view_func
            return None


if __name__ == '__main__':
    router = Router()