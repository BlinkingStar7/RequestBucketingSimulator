from simulator import *

if __name__ == "__main__":
    user_bucketing_simulator = Simulator()
    request_bucketing_simulator = Simulator()

    while not user_bucketing_simulator.is_over():
        id = user_bucketing_simulator.get_next_request()

        # user bucketing only allocate user to group based on their id
        if user_bucketing_simulator.can_allocate(id, id//SimulatorConstants.NUMBER_OF_PEOPLE_IN_GROUP.value):
            user_bucketing_simulator.allocate(id, id//SimulatorConstants.NUMBER_OF_PEOPLE_IN_GROUP.value)

    while not request_bucketing_simulator.is_over():
        id = request_bucketing_simulator.get_next_request()

        # request bucketing allocate user to group based on random number
        random_group = random.randint(0, SimulatorConstants.NUMBER_OF_GROUPS.value - 1)
        if request_bucketing_simulator.can_allocate(id, random_group):
            request_bucketing_simulator.allocate(id, random_group)

    # print a table of results
    print('User Bucketing')
    user_bucketing_simulator.print_results()
    print('Request Bucketing')
    request_bucketing_simulator.print_results()
