import unittest
from flask import Flask
from flask.ext import pigeon


class MsgTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask("APP")
        self.pigeon = pigeon.Pigeon(self.app)
        self.messages = pigeon.Messages()

    def test_tags(self):
        self.assertEquals(self.messages.INFO, "alert-info")
        self.assertEquals(self.messages.ERROR, "alert-error")
        self.assertEquals(self.messages.SUCCESS, "alert-success")
        self.assertEquals(self.messages.WARNING, "alert-block")


if __name__ == '__main__':
    unittest.main()
