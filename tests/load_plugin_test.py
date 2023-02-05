import unittest
import os

from akulai.akulai import AkulAI
class LoadPluginTest(unittest.TestCase):
    akulai = AkulAI()
    def test_check_info(self):
        self.akulai.check_info('test_root', 'test_file', '.py')
        self.assertTrue(os.path.isfile('test_root/test_file/plugin.info'))

if __name__ == '__main__':
    unittest.main()
