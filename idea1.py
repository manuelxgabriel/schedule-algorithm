import input_testing


class Teams:
    played = []

    def __init__(self, id, day):
        self.id = id
        self.day = day

    def print_info(self):
        print(f'Team: {self.id} Day: {self.day}')

def start():
    the_dict = input_testing.fixed_inputs

    team1 = Teams(1, 'Tuesday')
    team1.print_info()


start()

