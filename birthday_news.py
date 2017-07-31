import requests
import json
import urllib
import os
import textwrap
import datetime

#print introduction

def introduction():
    intro = """
    -------------
    Birthday News
    -------------

    This app will tell you a few things about the world on the day that you were born.
    Articles from the New York Times will be displayed for your birthday.

    """
    print(intro)

#get birth date from user

def get_bday():
    your_bday = input("Ok, so no judgments... when is your birthday? (YYYYMMDD): ")
    return your_bday

#check if today is the user's birthday

def is_it_today():
    today = datetime.datetime.today()
    if user_birthday[4:] == '{0:%m%d}'.format(today):
        print("""
##     ##    ###    ########  ########  ##    ##
##     ##   ## ##   ##     ## ##     ##  ##  ##
##     ##  ##   ##  ##     ## ##     ##   ####
######### ##     ## ########  ########     ##
##     ## ######### ##        ##           ##
##     ## ##     ## ##        ##           ##
##     ## ##     ## ##        ##           ##

########  #### ########  ######## ##     ## ########     ###    ##    ## ####
##     ##  ##  ##     ##    ##    ##     ## ##     ##   ## ##    ##  ##  ####
##     ##  ##  ##     ##    ##    ##     ## ##     ##  ##   ##    ####   ####
########   ##  ########     ##    ######### ##     ## ##     ##    ##     ##
##     ##  ##  ##   ##      ##    ##     ## ##     ## #########    ##
##     ##  ##  ##    ##     ##    ##     ## ##     ## ##     ##    ##    ####
########  #### ##     ##    ##    ##     ## ########  ##     ##    ##    #### """)

#create request to the NYTimes

def nytimes(birthday):
    data_request = {}
    data_request['api-key'] = os.environ["NYU_INFO_2335"]
    data_request['begin_date'] = birthday
    data_request['end_date'] = birthday

    url_values = urllib.parse.urlencode(data_request)
    basic_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    full_url = basic_url + '?' + url_values
    r = requests.get(full_url)
    nyt_data = r.json()
    #print(r.status_code)
    return nyt_data

#parse nyt_data

def parse_nyt_data(to_parse):

    print("\n", "We found ", len(to_parse['response']['docs']), " articles from the day that you were born!", "\n", sep="")

    i = 0
    while True:
        if to_parse['response']['docs'][i]['headline']['main'] == None:
            print("Article title not available.")
        else:
            print("\n")
            print("**", textwrap.fill(to_parse['response']['docs'][i]['headline']['main']), "**", "\n")
        if to_parse['response']['docs'][i]['snippet'] == None:
            print("Bummer... the article preview is not avaiable. Try the URL below.", "\n")
        else:
            print(textwrap.fill(to_parse['response']['docs'][i]['snippet']), "\n")
        print("Read the entire article: ")
        print(to_parse['response']['docs'][i]['web_url'], "\n", "\n")

        if i == (len(to_parse['response']['docs'])-1):
            break

        x = input("Press ENTER to see next article or 'done' to exit: ")
        if x.lower() == 'done':
            print("\n", "OK, Bye!", "\n")
            break
        i += 1

#-----------
#run the app
#-----------

introduction()

user_birthday = get_bday()

is_it_today()

articles = nytimes(user_birthday)

if len(articles['response']['docs']) == 0:
    print("\n", "No articles found for your birthdate... I guess you were all news that we needed! :-)", "\n", sep="")
else:
    parse_nyt_data(articles)
