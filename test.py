import unittest
from helper1 import get_club_by_mail


class test_helper(unittest.TestCase):

    def test_login(self):
        p = get_club_by_mail(mail="kate@shelifts.co.uk")
        club_exemple = {"name": "She Lifts",
                        "email": "kate@shelifts.co.uk",
                        "points": 12
                        }
        self.assertEqual(p,club_exemple)


if __name__ == '__main__':
    unittest.main()
