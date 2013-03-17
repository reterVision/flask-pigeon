"""
A simulation to Django's Messages Framework designed for Flask.
"""
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack
from flask import request
import constant


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

        if hasattr(app, "before_request"):
            app.before_request(self.before_request)

    def teardown(self, exception):
        pass

    def context_processor(self):
        return dict(messages=self.get_messages())

    def before_request(self):
        request._messages = []

    def add_messages(self, message):
        """Add a message to the request using Pigeon"""
        if hasattr(request, "_messages"):
            return request._messages.append(message)

    def get_messages(self):
        """Returns the messages stored in the request if it exists, otherwise
        returns an empty list.
        """
        if hasattr(request, "_messages"):
            return request._messages
        else:
            return []

    def info(self, message):
        self.add_messages({"tag": constant.INFO, "message": message})

    def error(self, message):
        self.add_messages({"tag": constant.ERROR, "message": message})

    def success(self, message):
        self.add_messages({"tag": constant.SUCCESS, "message": message})

    def warning(self, message):
        self.add_messages({"tag": constant.WARNING, "message": message})
