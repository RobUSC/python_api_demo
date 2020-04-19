from unittest import TestCase
from service.HelloWorldService import hello_world
import logging


class TestHelloWorldService(TestCase):
    def test_hello_world(self):
        logging.info('Hello World Test')
        self.assertEqual('Hello World!', hello_world())
