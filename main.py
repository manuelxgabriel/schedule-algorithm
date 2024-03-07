import input_testing
import random


def match_teams_by_preference(teams):
    matched_teams = []
    remaining_weeks = number_weeks

    for preference, team_ids in teams.items():
        # Shuffle the team ID to randomize the matches
        random.shuffle(team_ids)
        # Match teams with the same preference
        while len(team_ids) >= 2 and remaining_weeks > 0:
            matched_teams.append((team_ids.pop(), team_ids))
            remaining_weeks -= 1

    return matched_teams


# Function to match teams with 'No Preference' preference
def match_teams_no_preference(teams, no_preference_teams):
    matched_teams = []
    remaining_week = number_weeks
    teams_list = list(teams)
    random.shuffle(no_preference_teams)
    for team_id in no_preference_teams:
        if remaining_week <= 0:
            break
        # Match the team with another team randomly
        random_team = random.choice(teams_list)
        matched_teams.append((team_id, random_team))
        teams_list.remove(random_team)
        remaining_week -= 1

    return matched_teams

def group_team_preference(my_dict):
    preference_list = ['Tuesday', 'Friday', 'No Preference']
    groups = {}

    for preference in preference_list:
        groups[preference] = []

    for team in my_dict.values():
        preference = team[1]
        groups[preference].append(team)

    # for x in groups:
    #     print(groups[x])

    return groups


def create_schedule(matched_teams):
    week = 1
    remaining_weeks = number_weeks

    while remaining_weeks > 0:
        print(f"Week {week}:")
        for _ in range(9):
            if not matched_teams:
                break
            match = matched_teams.pop(0)
            print(f"   {match[0]} vs {match[1]}")
        week += 1
        remaining_weeks -= 1


def start():
    # Get the input data
    the_dict = input_testing.fixed_inputs

    # Get the teams based on their preference
    groups = group_team_preference(the_dict)

    # Match teams within the same preference
    matched_teams = match_teams_by_preference(groups)
    # print(match_teams_by_preference((groups)))

    # Extract teams with No Preference
    no_preference_teams = groups.get('No Preference', [])

    # Match teams with 'No Preference' preference with other teams
    matched_teams.extend(match_teams_no_preference(groups.values(), no_preference_teams))

    # Create schedule of the teams playing every week
    create_schedule(matched_teams)


number_weeks = 16
start()




