from ast import literal_eval
from random import choice, choices
import pandas as pd

class MemoryEvent:
    def __init__(self, description, weight, pos_a=[], neg_a=[], neu_a=[], s_e={}) -> None:
        """
        A memory has: 
        - description "" : line of text describing event
        - weight [0-5] : how impactful is this information?
        - positively_affects [] : list of siblings positively implicated
        - negatively_affects [] : list of siblings negatively implicated
        - neutraly_affects [] : list of siblings involved, but not impacted by memory
        - status_effects { trait : modifier } : dictionary of traits and their modifiers
        """
        self.description = description
        self.weight = weight
        self.positively_affects = pos_a
        self.negatively_affects = neg_a
        self.neutraly_affects = neu_a
        self.status_effects = s_e
        self.known_by = self.init_known()

    def init_known(self):
        """
        Simple init function for known_by.
        """
        known = []
        for l in [self.positively_affects, self.negatively_affects, self.neutraly_affects]:
            for p in l:
                if p not in known:
                    known.append(p)
        return known

    def char_knows(self, char_key):
        """
        Add new character to list of people who knows about it.
        """
        if char_key not in self.known_by:
            self.known_by.append(char_key)

    def does_char_know(self, char_key):
        """
        Checks if character knows about memory.
        """
        return char_key in self.known_by

    def how_affects_char(self, char_key):
        """
        Checks how character is affected by memory.
        """
        if char_key in self.positively_affects:
            return "positive"
        if char_key in self.negatively_affects:
            return "negative"
        if char_key in self.neutraly_affects:
            return "neutral"
        return "not affected"

class ChildhoodMemories:
    def __init__(self) -> None:
        self.memories = self.read_file()
        self.not_used = list(range(len(self.memories)))

    def read_file(self):
        fn = 'memoriesChild.csv'
        df = pd.read_csv(fn)
        for col in [
            'no_negative', 
            'no_neutral', 
            'no_positive', 
            'ch_decrease', 
            'ch_increase']:

            df[col].apply(lambda x: literal_eval(x) if isinstance(x, str) else x)
        return df

    def get_random(self):
        if self.not_used == []:
            return {}

        i = choice(self.not_used)
        self.not_used.remove(i)
        return dict(self.memories.iloc[i])





class Memory:
    def __init__(self) -> None:
        pass

c = ChildhoodMemories()
print(c.get_random())
