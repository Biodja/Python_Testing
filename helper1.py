import json
from datetime import datetime
from flask import flash
from exceptions import EmailNotFound

def load_clubs():
    with open("clubs.json") as file:
        return json.load(file)["clubs"]


def load_competitions():
    with open("competitions.json") as file:
        return json.load(file)["competitions"]


def get_club_by_mail(mail: str):
    
    try:
        
        selected_club = [club for club in CLUBS if club['email'] == mail][0]


    except IndexError:
        return None
    return selected_club


def get_club_by_name(name: str):
    selected_club = None
    for club in CLUBS:
        if club["name"] == name:
            selected_club = club
            break

    return selected_club


def get_competition_by_name(name: str):
    selected_competition = None
    for competition in COMPETITIONS:
        if competition["name"] == name:
            selected_competition = competition
            break

    return selected_competition


def get_max_places(club: dict):
    return min(int(club["points"]), 12)


def is_competition_date_correct(date: str):
    date_time_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    return datetime.today() > date_time_obj


def is_purchase_valid(competition: str, club: str, places: int):
    if not competition or not club:
        return False
    if not places.isnumeric():
        return False
    if int(places) > get_max_places(club=club):
        return False
    
    if is_purchase_valid:
        if int(club["points"]) != 0:
            club["points"] = int(club["points"]) - int(places)
      
      

    return True


COMPETITIONS = load_competitions()
CLUBS = load_clubs()
USER_CLUB = None