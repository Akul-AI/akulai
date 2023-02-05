import unittest
import os
from akulai.akulai import AkulAI

class AkulAITest(unittest.TestCase):
    def test_discover_plugins(self):
        akulai = AkulAI()

        # Test 1: Verify that the method discovers .py plugins
        os.makedirs("plugins/test_py")
        with open("plugins/test_py/test_py.py", "w") as f:
            f.write("# Test .py plugin")
        with open("plugins/test_py/plugin.info", "w") as f:
            f.write("dependencies: numpy\nauthor: Test Author\ndescription: Test .py plugin")
        akulai.discover_plugins()
        self.assertIn("test_py", akulai.plugins)
        self.assertEqual(".py", akulai.plugins["test_py"]["extension"])
        os.rmdir("plugins/test_py")

        # Test 2: Verify that the method discovers .js plugins
        os.makedirs("plugins/test_js")
        with open("plugins/test_js/test_js.js", "w") as f:
            f.write("// Test .js plugin")
        with open("plugins/test_js/plugin.info", "w") as f:
            f.write("dependencies: express\nauthor: Test Author\ndescription: Test .js plugin")
        akulai.discover_plugins()
        self.assertIn("test_js", akulai.plugins)
        self.assertEqual(".js", akulai.plugins["test_js"]["extension"])
        os.rmdir("plugins/test_js")

        # Test 3: Verify that the method discovers .pl plugins
        os.makedirs("plugins/test_pl")
        with open("plugins/test_pl/test_pl.pl", "w") as f:
            f.write("# Test .pl plugin")
        with open("plugins/test_pl/plugin.info", "w") as f:
            f.write("dependencies: DBI\nauthor: Test Author\ndescription: Test .pl plugin")
        akulai.discover_plugins()
        self.assertIn("test_pl", akulai.plugins)
        self.assertEqual(".pl", akulai.plugins["test_pl"]["extension"])
        os.rmdir("plugins/test_pl")


if __name__ == '__main__':
    unittest.main()
