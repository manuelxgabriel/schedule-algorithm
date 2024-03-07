import random

class Teams:
    def __init__(self, id, day):
        self.id = id
        self.day = day
        self.played = []

    def add_played_team(self, team_id):
        self.played.append(team_id)

    def print_info(self):
        print(f'Team: {self.id} Day: {self.day} Played: {self.played}')


class Roster:
    def __init__(self, teams):
        self.teams = teams


def create_schedule(teams):
    schedule = []
    teams_count = len(teams)
    for week in range(teams_count - 1):
        week_schedule = []
        for i in range(teams_count // 2):

            # Create a match with any teams
            match = (teams[i], teams[teams_count - 1 - i])
            week_schedule.append(match)

            # Add the opposite team
            teams[i].add_played_team(teams[teams_count - 1 - i].id)
            teams[teams_count - 1 - i].add_played_team(teams[i].id)

        # Add the weekly games to the schedule
        schedule.append(week_schedule)
        teams.insert(1, teams.pop())

    return schedule

def start():

    user_input = {
        "Tuesday": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "Friday": [10, 11, 12, 13],
        "No Preference": [14, 15, 16, 17, 18]
    }

    teams = []

    for day, ids in user_input.items():
        for id in ids:
            teams.append(Teams(id, day))

    schedule = create_schedule(teams)

    week_number = 1
    for week_schedule in schedule:
        print(f'Week {week_number} Schedule: ')
        for match in week_schedule:
            print(f'{match[0].id} vs {match[1].id}')
        week_number += 1


start()
