from datetime import datetime, timedelta
import unittest
from exceptions import EmailNotFound, ClubNotEnoughPoints, CompetitionNotEnoughPlaces, BookingLimitPlaces, CompetitionIsClosed
from helper1 import get_club_by_mail, is_purchase_valid, is_competition_date_correct, get_club_by_name, get_competition_by_name, load_competitions, load_clubs
from server import app 


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


class TestFormBooking(unittest.TestCase):

    def setUp(self):
        self.club = {"name": "She Lifts",
                     "email": "kate@shelifts.co.uk",
                     "points": "8"
                     }
        self.competition = {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }

        self.clients = app.test_client()

# Un test pour s'assurer que les places demandé ne depasse pas les points du club
    def test_exception_is_raised_if_places_required_are_greater_than_points_club(self):



            self.assertEqual(is_purchase_valid(self.competition, self.club, "10"), False)

# Un test pour s'assurer que les places demandé ne depasse pas les points de la compétitions
    def test_exception_is_raised_if_places_required_are_greater_than_competition_places(self):
        self.assertEqual(is_purchase_valid(None, self.club, "16"),False)
            
            

# Un test pour s'assurer que les places demandé ne depasse pas les points du club et de la compétitions
    def test_return_if_places_required_are_less_or_equal_than_points_club_and_competition_places(self):
        self.assertEqual(is_purchase_valid(self.competition, None, "16"), False)

# Un test qui retourne une exeption si les places demandé ne depasse pas la limite de la compétitions
    def test_exception_is_raised_if_places_required_are_greater_than_limit_booking_places(self):
        self.assertEqual(is_purchase_valid(self.competition, self.club, "8"), True)
            

# teste si la compétition est valide
    def test_exception_is_raised_if_competition_is_closed(self):
        date = datetime.now() - timedelta(days=1)
        str_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(is_competition_date_correct(str_date),True)

# teste si la compétition n'est pas valide
    def test_exception_not_raised_if_competition_is_not_closed(self):
        date = datetime.now() + timedelta(days=1)
        str_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(is_competition_date_correct(str_date),False)

# test de la page d'acceuil
    def test_get_home_page(self):
        reponse = self.clients.get("/", follow_redirects=True)
        self.assertEqual(b"<h1>Welcome to the GUDLFT Registration Portal!</h1>" in reponse.data, True)
        self.assertEqual(reponse.status_code , 200)


# test show summary
    def test_show_summary(self):
        reponse = self.clients.post("/showSummary",data={"email": "a@gmail.com"}, follow_redirects=True)
        self.assertEqual(b"Sorry, that email" in reponse.data, True)
        self.assertEqual(reponse.status_code , 200)


# test booking
    def test_booking(self):
       reponse = self.clients.get("/book/<competition>/<club>", follow_redirects=True)
       self.assertEqual(b"book" in reponse.data, True)
       self.assertEqual(reponse.status_code , 200)
    

    def test_logout(self):
        reponse = self.clients.get("/logout", follow_redirects=True)

        self.assertEqual(reponse.status_code , 200)
    

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
