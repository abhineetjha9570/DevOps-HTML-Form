from pathlib import Path
import unittest

HTML_FILE = Path(__file__).parent / "index.html"


class HTMLFormTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html = HTML_FILE.read_text(encoding="utf-8")

    def test_form_exists(self):
        self.assertIn('<form id="registrationForm">', self.html)

    def test_name_input_exists(self):
        self.assertIn('id="name"', self.html)

    def test_email_input_exists(self):
        self.assertIn('type="email"', self.html)

    def test_contact_input_exists(self):
        self.assertIn('id="contact"', self.html)

    def test_required_fields_exist(self):
        self.assertEqual(self.html.count("required>"), 3)

    def test_submit_button_exists(self):
        self.assertIn('type="submit"', self.html)


if __name__ == "__main__":
    unittest.main(verbosity=2)