import unittest
from models.app import App
from models.library import Library


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_add_library(self):
        self.app.add_library()
        self.assertEqual(len(self.app.libraries), 1)

    def test_select_library(self):
        library = Library("Test Library")
        self.app.libraries.append(library)
        self.app.select_library()
        self.assertEqual(self.app.current_library, library)


if __name__ == "__main__":
    unittest.main()
