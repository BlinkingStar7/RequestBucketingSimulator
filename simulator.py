import random
from enum import Enum


class SimulatorConstants(Enum):
    NUMBER_OF_GROUPS = 3
    NUMBER_OF_PEOPLE_IN_GROUP = 100
    IMPRESSION_MAX_PER_GROUP = 1000
    CPU = 2


class Simulator:
    def __init__(self):
        # generate population (id, pctr)
        self.population = [(i, random.randint(0, 100)) for i in range(SimulatorConstants.NUMBER_OF_GROUPS.value * SimulatorConstants.NUMBER_OF_PEOPLE_IN_GROUP.value)]

        # count number of imp and clicks per group
        self.impressions = [0] * SimulatorConstants.NUMBER_OF_GROUPS.value
        self.clicks = [0] * SimulatorConstants.NUMBER_OF_GROUPS.value

        # store map of imp and click users' ids
        self.unique_impressions = [{} for _ in range(SimulatorConstants.NUMBER_OF_GROUPS.value)]
        self.unique_clicks = [{} for _ in range(SimulatorConstants.NUMBER_OF_GROUPS.value)]

    # mimic ad request by pick random index among population
    def get_next_request(self):
        id = random.randint(0, len(self.population) - 1)
        return id

    # check user with id can be allocated to group
    def can_allocate(self, id, group):
        if self.impressions[group] >= SimulatorConstants.IMPRESSION_MAX_PER_GROUP.value:
            return False
        return True

    def can_click(self, id, group):
        return random.randint(0, 99) < self.population[id][1] and self.unique_clicks[group].get(id, 0) < SimulatorConstants.CPU.value

    # allocate user with id to group
    def allocate(self, id, group):
        self.unique_impressions[group][id] = self.unique_impressions[group].get(id, 0) + 1
        self.impressions[group] += 1

        if self.can_click(id, group):
            self.unique_clicks[group][id] = self.unique_clicks[group].get(id, 0) + 1
            self.clicks[group] += 1

    def get_unique_click(self, group):
        return len(self.unique_clicks[group])

    def get_unique_imp(self, group):
        return len(self.unique_impressions[group])

    def get_click_count(self, group):
        return self.clicks[group]

    def get_imp_count(self, group):
        return self.impressions[group]

    # check if all group has reached max impressions
    def is_over(self):
        for imp in self.impressions:
            if imp < SimulatorConstants.IMPRESSION_MAX_PER_GROUP.value:
                return False
        return True

    def print_results(self):
        print('-' * 50)
        print('Group\tImp\tClick\tUnique Imp\tUnique Click')
        for i in range(SimulatorConstants.NUMBER_OF_GROUPS.value):
            print(f'{i}\t{self.impressions[i]}\t{self.clicks[i]}\t{len(self.unique_impressions[i])}\t\t{len(self.unique_clicks[i])}')
        print('-' * 50)
        print('Total\t' + f'{sum(self.impressions)}\t{sum(self.clicks)}\t{sum(len(self.unique_impressions[i]) for i in range(SimulatorConstants.NUMBER_OF_GROUPS.value))}\t\t{sum(len(self.unique_clicks[i]) for i in range(SimulatorConstants.NUMBER_OF_GROUPS.value))}')
        print('\n')