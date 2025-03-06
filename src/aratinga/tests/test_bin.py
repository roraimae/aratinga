import os
import shutil
import sys
import unittest

from aratinga.bin import main as cms_main


class TestCmsStart(unittest.TestCase):
    CURR_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEST_DIR = os.path.join(CURR_DIR, "testproject-unittest")

    def setup(self):
        # Clean/create directory to start into
        if os.path.exists(self.TEST_DIR):
            shutil.rmtree(self.TEST_DIR)
        os.mkdir(self.TEST_DIR)

    def cleanup(self):
        # Cleanup
        if os.path.exists(self.TEST_DIR):
            shutil.rmtree(self.TEST_DIR)

    def test_help(self):
        # Set args
        sys.argv = ["cms_main", "help"]
        # Runpyt
        cms_main()
        # Nothing to assert here... just make sure it doesn't error out.

    def test_help_start(self):
        # Set args
        sys.argv = ["cms_main", "help", "start"]
        # Run
        cms_main()
        # Nothing to assert here... just make sure it doesn't error out.

    def test_default(self):
        self.setup()
        # Set args
        sys.argv = ["cms_main", "start", "myproject", self.TEST_DIR]
        # Run
        cms_main()
        # Assert files exist
        self.assertTrue(os.path.exists(os.path.join(self.TEST_DIR, "README.md")))
        self.cleanup()

    def test_allopts(self):
        self.setup()
        # Set args
        sys.argv = [
            "cms_main",
            "start",
            "myproject",
            self.TEST_DIR,
            "--sitename",
            "Instituição de Ensino Superior",
            "--domain",
            "example.com",
        ]
        # Run
        cms_main()
        # Assert files exist
        self.assertTrue(os.path.exists(os.path.join(self.TEST_DIR, "README.md")))
        self.cleanup()

    def test_domain_www(self):
        self.setup()
        # Set args
        sys.argv = [
            "cms_main",
            "start",
            "myproject",
            self.TEST_DIR,
            "--domain",
            "www.example.com",
        ]
        # Run
        cms_main()
        # Assert files exist
        self.assertTrue(os.path.exists(os.path.join(self.TEST_DIR, "README.md")))
        self.cleanup()
