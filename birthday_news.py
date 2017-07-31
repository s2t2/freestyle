import requests
import json
import urllib
import os
import textwrap
import datetime

def introduction():
    intro = """
    -------------
    Birthday News
    -------------

    This app will tell you a few things about the world on the day that you were born.
    Articles from the New York Times will be displayed for your birthday.

    """
    print(intro)











#-----------
#run the app
#-----------

introduction()

user_birthday = get_bday()

is_it_today()

articles = nytimes(user_birthday)

parse_nyt_data(articles)
