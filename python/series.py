#!/usr/bin/env python
"""
Tracks your progress on any series!
Usage:
-a: use -a name_of_show to add a new show
-e: use -e name_of_show [num] to add num to episodes or ommit num to add 1
-s: use -s name_of_show [num] to add num to seasons or ommit num to add 1
-d: use -d name_of_show to delete the show
-f: use -f search_string to display shows that match the search string
help: Prints this help text

Note that changing the season sets the episode to 1

Author: Tim Silhan
"""

import sys
import json
import os.path

# Save file where all the series data will be saved
SAVE_FILE = "series_data.json"

def main():
    """ Main logic of the script packed in main for readability """

    print("-------------------------")
    print("|Series Progress Tracker|")
    print("-------------------------")
    print("")

    shows = []
    if os.path.isfile(SAVE_FILE):
        shows = read_series()

    # TODO: Restructure to remove redundancy of checking number of arguments

    # Print all the shows if no arguments are passed
    if len(sys.argv) == 1:
        print_series(shows)
        sys.exit()

    if sys.argv[1] == "help":
        print_help()
        sys.exit()

    if sys.argv[1] == "-a":
        # Add the new series
        # If there is no series name or it is empty do not create a series
        if len(sys.argv) != 3 or sys.argv[2] == "":
            print("You have to provide the name of the series as a second argument")
            sys.exit()

        shows.append(Series(sys.argv[2]))

    if sys.argv[1] == "-e" or sys.argv[1] == "-s":
        # If there is no series name or it is empty do not create a series
        if len(sys.argv) < 3:
            print("You have to provide the name of the series as a second argument")
            sys.exit()

        filtered_shows = filter_shows(shows, sys.argv[2])
        show = select_show(filtered_shows)

        if show is None:
            print("This show does not exist")
            sys.exit()

        # Update the episode or season of the show
        update_series(show, sys.argv[1], 1 if len(sys.argv) == 3 else int(sys.argv[3]))

    if sys.argv[1] == "-d":
        if len(sys.argv) < 3:
            print("You have to provide the name of the series as a second argument")
            sys.exit()

        filtered_shows = filter_shows(shows, sys.argv[2])
        show = select_show(filtered_shows)

        if show is None:
            print("This show does not exist")
            sys.exit()

        shows.remove(show)

    if sys.argv[1] == "-f":
        # If there is no series name or it is empty do not create a series
        if len(sys.argv) < 3:
            print("You have to provide the name of the series as a second argument")
            sys.exit()

        print_series(filter_shows(shows, sys.argv[2]))
        sys.exit()

    write_series(shows)
    print_series(shows)


class Series:
    """ Represents the data structure of a series """

    def __init__(self, name, season=1, episode=1):
        self.name = name
        self.season = season
        self.episode = episode

    def __repr__(self):
        return "{}: Season {} Episode {}".format(self.name, self.season, self.episode)

def read_series():
    """ Reads all the shows from the save file """
    shows = []
    with open(SAVE_FILE, 'r') as infile:
        series_data = json.load(infile)
        for s in series_data:
            shows.append(Series(s['name'], s['season'], s['episode']))

    return shows

def write_series(shows):
    """ Writes all the shows to the save file """
    with open(SAVE_FILE, 'w') as outfile:
        json.dump([ob.__dict__ for ob in shows], outfile)

def print_series(shows):
    """ Prints all the shows """
    for show in shows:
        print(show)

def print_help():
    """ Prints information regarding the usage of this script """

    print(("Tracks your progress on any series!\n"
           "Usage:\n"
           "-a: use -a name_of_show to add a new show\n"
           "-e: use -e name_of_show [num] to add num to episodes or ommit num to add 1\n"
           "-s: use -s name_of_show [num] to add num to seasons or ommit num to add 1\n"
           "-d: use -d name_of_show to delete the show\n"
           "-f: use -f search_string to display shows that match the search string\n"
           "help: Prints this help text\n"
           "\n"
           "Note that changing the season sets the episode to 1\n"))

def update_series(series, command, amount):
    """ Updates a series """
    if command == "-e":
        series.episode += amount
    elif command == "-s":
        series.season += amount
        series.episode = 1

def filter_shows(shows, search_string):
    """ Filters the list of shows by a search string """

    # Get all the shows that contain the search string in their name
    # This search is not case-sensitive
    return list(filter(lambda x: search_string.lower() in x.name.lower(), shows))


def select_show(shows):
    """ Gets a list of shows and makes the user choose one """
    if len(shows) == 0:
        return None
    if len(shows) == 1:
        # If there is only one show that matches the search string return it immediately
        return shows[0]
    else:
        # Otherwise the user has to choose one of the options
        print("Choose a show:")
        for index, item in enumerate(shows):
            print("({}) {}".format(index + 1, item.name))

        # Read the users input
        user_input = input("\nYour choice (1 - {}): ".format(len(shows)))
        print()

        if not is_number(user_input):
            print("Invalid input")
            sys.exit()

        index = int(user_input) - 1
        if index >= 0 and index < len(shows):
            return shows[index]
     
        return None

def is_number(num):
    """ Checks if num can be cast to an int """
    try:
        int(num)
        return True
    except ValueError:
        return False

main()
