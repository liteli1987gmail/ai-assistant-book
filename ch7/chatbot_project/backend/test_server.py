import unittest
from server import get_gpt4_answer

class TestServer(unittest.TestCase):
    def test_get_gpt4_answer(self):
        self.assertEqual(get_gpt4_answer('Hello, world!'), 'Hello, human!')

if __name__ == '__main__':
    unittest.main()