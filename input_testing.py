import random

# Tuesday = 3
# Friday = 6
# No Preference = 8
fixed_inputs = {
    0: [0, 'No Preference'],
    1: [1, 'Friday'],
    2: [2, 'No Preference'],
    3: [3, 'Tuesday'],
    4: [4, 'No Preference'],
    5: [5, 'Friday'],
    6: [6, 'No Preference'],
    7: [7, 'No Preference'],
    8: [8, 'No Preference'],
    9: [9, 'Friday'],
    10: [10, 'Friday'],
    11: [11, 'Tuesday'],
    12: [12, 'No Preference'],
    13: [13, 'Friday'],
    14: [14, 'Tuesday'],
    15: [15, 'No Preference'],
    16: [16, 'Friday'],
    17: [17, 'Tuesday']

}

fixed_inputs_sorted = {
    0: [0, 'No Preference'],
    2: [2, 'No Preference'],
    4: [4, 'No Preference'],
    6: [6, 'No Preference'],
    7: [7, 'No Preference'],
    8: [8, 'No Preference'],
    12: [12, 'No Preference'],
    15: [15, 'No Preference'],

    1: [1, 'Friday'],
    5: [5, 'Friday'],
    9: [9, 'Friday'],
    10: [10, 'Friday'],
    16: [16, 'Friday'],
    13: [13, 'Friday'],

    3: [3, 'Tuesday'],
    11: [11, 'Tuesday'],
    14: [14, 'Tuesday'],
    17: [17, 'Tuesday']

}


def get_random_inputs() -> dict:
    number_teams = 18
    number_weeks = 16
    my_dict = {}

    tuesday = 0
    friday = 0
    no_preference = 0

    # Get the random preferred day (Tuesday or Friday)
    for x in range(number_teams):
        random_num = random.randint(0,2)
        my_dict[x] = ["id","value1", 0]

        if random_num == 0:
            random_day = "Tuesday"
        elif random_num == 1:
            random_day = "Friday"
        else:
            random_day = "No Preference"

        my_dict[x][0] = x
        my_dict[x][1] = random_day
        if my_dict[x][0] == "Tuesday":
            tuesday += 1
        elif my_dict[x][0] == 'Friday':
            friday += 1
        else:
            no_preference += 1

    # print(f"Number of teams that choose Tuesday: {tuesday}")
    # print(f"Number of teams that choose Friday: {friday}")
    # print(f"Number of teams that choose Friday: {no_preference}")

    return my_dict
