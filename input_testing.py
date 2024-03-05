import random

# Tuesday = 3
# Friday = 6
# No Preference = 8
fixed_inputs = {
    0: [0, 'No Preference', 0],
    1: [1, 'Friday', 0],
    2: [2, 'No Preference', 0],
    3: [3, 'Tuesday', 0],
    4: [4, 'No Preference', 0],
    5: [5, 'Friday', 0],
    6: [6, 'No Preference', 0],
    7: [7, 'No Preference', 0],
    8: [8, 'No Preference', 0],
    9: [9, 'Friday', 0],
    10: [10, 'Friday', 0],
    11: [11, 'Tuesday', 0],
    12: [12, 'No Preference', 0],
    13: [13, 'Friday', 0],
    14: [14, 'Tuesday', 0],
    15: [15, 'No Preference', 0],
    16: [16, 'Friday', 0],
    17: [17, 'Tuesday', 0]
}


number_teams = 18
number_weeks = 16
my_dict = {}


def get_random_inputs() -> dict:
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
