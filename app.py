# py-02-basketball-team-stats

from constants import TEAMS as original_teams
from constants import PLAYERS as original_players


def clean_data():
    pass


def balance_teams():
    pass


def start():
    print(original_teams)
    print()
    print(original_players)
    pass


if __name__ == "__main__":
    start()


'''
PROJECT GOALS
=============
    01) CREATE A NEW SCRIPT

    02) PROPER USER OF DUNDER MAIN

    03) IMPORT PLAYER DATA

    04) CREATE A CLEAN_DATA FUNCTION
        01) Read the existing player data from the PLAYERS constants
        02) Clean the player data WITHOUT CHANGING THE ORIGINAL DATA
            01) Height: This should be saved as an INTEGER
            02) Experience: This should be saved as a BOOLEAN VALUE
        03) Save the cleaned data to a new collection
    05) create a balance_teams function

    06) Console readability matters

    07) displaying the stats
        01) Team's name as a string
        02) Total players on that team as an integer
        03) The player names as strings separated by commas

EXTRA CREDIT
============
    01) cleaning the guardian field
    02) additional balancing to the team
    03) include additional stats for a given displayed team
        01) number of inexperience players on that team
        02) number of experienced players on that team
        03) the average height of the team
        04) the guardians of all the players on that team (as a comma-separated            string)
    04) quite menu option
'''
