"""
A simulation to Django's Messages Framework designed for Flask.
"""
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class Messages(object):
    INFO = "alert-info"
    ERROR = "alert-error"
    SUCCESS = "alert-success"
    WARNING = "alert-block"

    def __init__(self, tag=INFO, message=""):
        self.tag = tag
        self.message = message

    def __call__(self):
        return {"messages": self}


class Pigeon(object):
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    _messages = []

    def init_app(self, app):
        if hasattr(app, "teardown_appcontext"):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

        if hasattr(app, "context_processor"):
            app.context_processor(self.context_processor)

    def teardown(self, exception):
        pass

    def context_processor(self):
        context_messages = list(self._messages)
        self._messages = []  # Clear the messages array.
        return dict(messages=context_messages)

    def info(self, message):
        self._messages.append(Messages(Messages.INFO, message))

    def error(self, message):
        self._messages.append(Messages(Messages.ERROR, message))

    def success(self, message):
        self._messages.append(Messages(Messages.SUCCESS, message))

    def warning(self, message):
        self._messages.append(Messages(Messages.WARNING, message))
