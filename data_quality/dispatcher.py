from threading import Lock

class PathDispatcher:
    def __init__(self, default_app, create_app):
        self.default_app = default_app
        self.create_app = create_app
        self.lock = Lock()
        self.instances = {}

    def get_application(self, prefix):
        with self.lock:
            app = self.instances.get(prefix)
            if app is None:
                app = self.create_app(prefix)
                if app is not None:
                    self.instances[prefix] = app
            return app

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '').lstrip('/')
        parts = path.split('/', 1)
        prefix = parts[0] if parts else ''
        
        app = self.get_application(prefix)
        if app is not None:
            environ['PATH_INFO'] = '/' + (parts[1] if len(parts) > 1 else '')
        else:
            app = self.default_app
        return app(environ, start_response)