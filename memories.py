from ast import literal_eval
from random import choice, randint, random
import pandas as pd
from copy import copy

class ChildhoodMemories:
    def __init__(self) -> None:
        self.memories = self.read_file()
        self.not_used = list(range(len(self.memories)))

    def read_file(self):
        fn = 'input/memoriesChild.csv'
        df = pd.read_csv(fn)
        return df

    def get_random(self):
        if self.not_used == []:
            return {}

        i = choice(self.not_used)
        self.not_used.remove(i)

        rm = dict(self.memories.iloc[i])
        return rm


class AdultMemories:
    def __init__(self) -> None:
        pass

class Memory:
    def __init__(self, name) -> None:
        self.name = name
        self.childhood_memories = {}

    def add_childhood_memory(self, memory):
        changes = {}
        m = copy(memory)
        m['description'] = m['description'].replace(self.name, 'I')
        x = m['mapping'].values()
        people = list(filter(None, x))
        m['people'] = people 

        # alter relationships
        changes['relationships'] = {}
        if m['memory_relation_impact'] == 'neutral': 
            r_mod = 0
        else: 
            r_mod = -1 if m['memory_relation_impact'] == 'negative' else 1

        r_ch = randint(1, 20)
        if self.name == m['mapping']['me']:
            for p in people: 
                if self.name != p: 
                    changes['relationships'][p] = r_mod * r_ch 
        else: 
            originator = m['mapping']['me']
            changes['relationships'][originator] = r_mod * r_ch 

        # cleanup
        m.pop('mapping')
        m.pop('base_chance')

        # memory is not always remembered
        if random() < 0.7:
            for p in people:
                if p == self.name:
                    p = 'myself'
                if p not in self.childhood_memories:
                    self.childhood_memories[p] = {}
                self.childhood_memories[p][m['keyword']] = m

        return changes

    def add_pre_config_childhood_memory(self, m, about_person):
        if about_person not in self.childhood_memories:
            self.childhood_memories[about_person] = {}

        key = m['keyword']
        self.childhood_memories[about_person][key] = m

    def add_memory(self, memory):
        pass

    def get_memory(self): 
        return self.childhood_memories

# c = ChildhoodMemories()
# a = c.get_random()
# print(a)
# m = Memory()
# m.add_childhood_memory(a)
# print(m.childhood_memories)
