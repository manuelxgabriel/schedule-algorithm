def round_robin(units, sets=None):
    """ Generates a schedule of "fair" pairings from a list of units """
    count = len(units)
    sets = sets or (count - 1)
    half = count // 2  # Use integer division to get integer result
    for turn in range(sets):
        left = units[:half]
        right = units[count - half - 1 + 1:][::-1]
        pairings = zip(left, right)
        if turn % 2 == 1:
            pairings = [(y, x) for (x, y) in pairings]
        units.insert(1, units.pop())
        yield list(pairings)  # Convert zip object to list before yielding

teams = ['a', 'b', 'c', 'd']
for schedule in round_robin(teams, sets=len(teams) * 2 - 2):
    print(schedule)
