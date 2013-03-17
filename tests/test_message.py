import unittest
from flask import Flask
from flask.ext import pigeon


class MsgTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask("APP")
        self.pigeon = pigeon.Pigeon(self.app)

    def test_tags(self):
        self.pigeon.info("INFO")
        self.pigeon.error("ERROR")
        self.pigeon.success("SUCCESS")
        self.pigeon.warning("WARNING")

        message_list = self.pigeon.get_messages()

        self.assertEquals(message_list[0].tag, "alert-info")
        self.assertEquals(message_list[0].message, "INFO")
        self.assertEquals(message_list[1].tag, "alert-error")
        self.assertEquals(message_list[1].message, "ERROR")
        self.assertEquals(message_list[2].tag, "alert-success")
        self.assertEquals(message_list[2].message, "SUCCESS")
        self.assertEquals(message_list[3].tag, "alert-block")
        self.assertEquals(message_list[3].message, "WARNING")


if __name__ == '__main__':
    unittest.main()
