import unittest

from akulai.akulai import AkulAI

class ListenTest(unittest.TestCase):
    akulai = AkulAI()

    def test_listen(self):
        self.assertTrue(self.akulai.listening_thread.is_alive())
        self.akulai.stop_listening.set()
        self.akulai.listening_thread.join()

if __name__ == '__main__':
    unittest.main()