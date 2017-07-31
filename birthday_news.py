import requests
import json
import urllib
import os
import textwrap
import datetime













#-----------
#run the app
#-----------

introduction()

user_birthday = get_bday()

is_it_today()

articles = nytimes(user_birthday)

parse_nyt_data(articles)
