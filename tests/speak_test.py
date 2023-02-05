import unittest

from akulai.akulai import AkulAI
class SpeakTest(unittest.TestCase):
    akulai = AkulAI()

    def test_speak(self):
        self.assertTrue(self.akulai.speaking_thread.is_alive())
        self.akulai.stop_speaking.set()
        self.akulai.speaking_thread.join()

if __name__ == '__main__':
    unittest.main()