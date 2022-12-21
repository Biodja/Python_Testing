from datetime import datetime, timedelta
import unittest
from exceptions import EmailNotFound, ClubNotEnoughPoints, CompetitionNotEnoughPlaces, BookingLimitPlaces, CompetitionIsClosed
from helper1 import get_club_by_mail, is_purchase_valid, is_competition_date_correct, get_club_by_name, get_competition_by_name, load_competitions, load_clubs
from server import app 

# test unitaire qui permet de tester des fonctions simple d'un code unité de code


class test_email(unittest.TestCase):
    # test de connexion par email
    def test_login(self):
        p = get_club_by_mail(mail="kate@shelifts.co.uk")
        club_exemple = {"name": "She Lifts",
                        "email": "kate@shelifts.co.uk",
                        "points": 12
                        }
        self.assertEqual(p, club_exemple)

# tester le club retourné si l'e-mail n'existe pas
    def test_exception_is_raised_if_email_does_not_exist(self):
        wrong_email = ('email')
        with self.assertRaises(EmailNotFound):
            
            get_club_by_mail(wrong_email)
            raise EmailNotFound
     

# tester le club retourné si l'e-mail existe
    def test_returned_club_if_email_does_exist(self):
        club = get_club_by_mail('kate@shelifts.co.uk')
        self.assertEqual(club['name'], 'She Lifts')


class test_load_data(unittest.TestCase):

    def test_load_json(self):
        clubs = {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points": 13
        }
        competitions ={
         "name": "Fall Classic",
         "date": "2020-10-22 13:30:00",
         "numberOfPlaces": "13"
     }
        p = load_clubs()
        s = load_competitions()
        self.assertEqual(p[0], clubs)
        self.assertEqual(s[1],competitions )

    
if __name__ == '__main__':
    unittest.main()
