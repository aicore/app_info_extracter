from mockito import mock, verify
import unittest

from hello_world import hello_world

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        hello_world(out)

        verify(out).write("Hello world of Python\n")