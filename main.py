import input_testing


# Compare if the teams are equal
# def compare_teams(my_dict):
#     number_teams = 18
#     number_weeks = 16
#
#     for i in range(number_teams):
#         for j in range(i + 1, number_teams):
#             if my_dict[i][0] == my_dict[j][0]:
#                 my_dict[i][1] += 1
#                 my_dict[j][1] += 1


# Match the teams to there preference
def matching_teams(my_dict) -> True:
    return False


# Group the teams into there preference
def group_team_preference(my_dict) :
    preference_list = ['Tuesday', 'Friday', 'No Preference']
    group_a = []
    group_b = []
    group_c = []

    for x in range(input_testing.number_teams):
        if my_dict[x][1] == preference_list[0]:
            group_a.append(my_dict[x])
        elif my_dict[x][1] == preference_list[1]:
            group_b.append(my_dict[x])
        else:
            group_c.append(my_dict[x])

    # for x in range(len(group_A)):
    #     print(group_A[x])


def start():
    the_dict = input_testing.fixed_inputs

    # Print out the dictionary
    for key, value in the_dict.items():
        print(f"{key}: {value[0]}, {value[1]}, {value[2]} ")

    # Compare with days the teams is playing on there preferred day
    # compare_teams(my_dict)
    # matching_teams(my_dict)
    #group_team_preference(my_dict)



start()


