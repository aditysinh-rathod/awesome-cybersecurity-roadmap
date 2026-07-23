import unittest
from utils import generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        password = generate_password(16)
        self.assertEqual(len(password), 16)

    def test_password_type(self):
        password = generate_password(12)
        self.assertIsInstance(password, str)

    def test_multiple_passwords_are_different(self):
        p1 = generate_password(16)
        p2 = generate_password(16)
        self.assertNotEqual(p1, p2)


if __name__ == "__main__":
    unittest.main()
