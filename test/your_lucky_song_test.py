import unittest
from your_lucky_song import your_lucky_song as yls


class MyTestCase(unittest.TestCase):
    def test_something(self):
        user = yls(1, 1, 1990)
        song_recommend = user.feel_lucky()
        self.assertEqual(song_recommend, 'https://www.youtube.com/watch?v=Qt2mbGP6vFI')


if __name__ == '__main__':
    unittest.main()
