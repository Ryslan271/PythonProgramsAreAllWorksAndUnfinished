import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_single_chat(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrome(self):
        self.assertEqual(reverse('aba'), 'aba')

    def test_common(self):
        self.assertEqual(reverse('cs'), 'sc')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_iterable(self):
        with self.assertRaises(TypeError):
            reverse(['a', 'b', 'c'])


if __name__ == '__main__':
    unittest.main()
