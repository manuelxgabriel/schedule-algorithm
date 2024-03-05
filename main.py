import input_testing


# Match the teams to there preference
def matching_teams(sorted_dict):
    preference_list = ['Tuesday', 'Friday', 'No Preference']
    seen_numbers = []

    for group in sorted_dict:
        for i in range(len(group)):
            current_team = group[i]
            for j in range(i + 1, len(group)):
                compared_team = group[j]
                print(f"{current_team[0]} vs {compared_team[0]}")
                seen_numbers.append(compared_team[0])
            current_team[3].extend(seen_numbers)
            seen_numbers.clear()


def group_team_preference(my_dict):
    preference_list = ['Tuesday', 'Friday', 'No Preference']
    groups = {preference: [] for preference in preference_list}

    for team in my_dict.values():
        preference = team[1]
        groups[preference].append(team)

    return groups.values()

# Group the teams into there preference
# def group_team_preference(my_dict):
#     preference_list = ['Tuesday', 'Friday', 'No Preference']
#     group_a = []
#     group_b = []
#     group_c = []
#
#     for x in range(input_testing.number_teams):
#         if my_dict[x][1] == preference_list[0]:
#             group_a.append(my_dict[x])
#         elif my_dict[x][1] == preference_list[1]:
#             group_b.append(my_dict[x])
#         else:
#             group_c.append(my_dict[x])
#
#     return_groups = [group_a, group_b, group_c]
#
#     return return_groups


def start():
    the_dict = input_testing.fixed_inputs
    sorted_groups = group_team_preference(the_dict)
    matching_teams(sorted_groups)

    # Print out the dictionary
    # for key, value in the_dict.items():
    #     print(f"{key}: {value[0]}, {value[1]}, {value[2]} ")


start()


