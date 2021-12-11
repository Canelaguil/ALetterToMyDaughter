import random
import pprint

traits = ['apathetic', 'disorganised', 'anxious', 'critical', 'quirky',
          'egocentric', 'creative', 'moral', 'impulsive', 'happy', 'obedient' 'brave']


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


class Juana:
    def __init__(self, input_file='') -> None:
        self.name = "Juana"
        self.surname = "Huijzen"
        self.known_traits = ['kind', 'moody']
        self.my_traits = ['kind', 'moody']
        self.trauma = random.randint(0, 50)
        self.country_affinities = {
            'Netherlands': 0, 'Spain': 0, 'Australia': 0}
        self.set_up()
        self.backstory = self.backstory()
        self.output_child()

    def set_up(self, input_file=''):
        # Get traits
        while len(self.my_traits) < 5:
            t = random.choice(traits)
            if t not in self.my_traits:
                self.my_traits.append(t)

        # Country affinities
        for country in self.country_affinities:
            self.country_affinities[country] = random.randint(-3, 3)

    def backstory(self):
        father_alive = True
        story = "I was born in Spain, where my parents met while fighting for the Spanish " + \
                "civil war. " 
        
        if random.random() < 0.5: 
            story += "My mother was a fervent communist, one of the leaders of " + \
                     "The Cause. My father had travelled there all the way from the Netherlands. But "
        else:
            story += "My mother was a victim of class and circumstance. She hardly knew how to read, " + \
                     "she was a communist because everyone else she knew was. My father on the other hand " + \
                     "had come all the way from the Netherlands to fight for the cause. But "

        if random.random() < 0.5:
            story += "he never came back. Right before the communists lost, my mother packed " + \
                     "up and took me to the Netherlands. She didn't even speak the language. " + \
                     "Her dark, Spanish features got us mistaken for Jews."

            father_alive = False 
            self.trauma += random.randint(0, 20)
            self.country_affinities['Spain'] = min(self.country_affinities['Spain'] + 2, 3)
            self.country_affinities['Netherlands'] = max(self.country_affinities['Netherlands'] - 2, -3)
        else:
            story += "in the war he lost my mother and with her his faith in the cause and " + \
                     "humanity at large. He took me back to the Netherlands." 
            self.country_affinities['Netherlands'] = min(self.country_affinities['Netherlands'] + 2, 3)

        self.age1940 = random.randint(9, 14)
        parent = 'father' if father_alive else 'mother'
        parent_pronoun = 'he' if father_alive else 'she'
        circumstance = 'knew he was a communist' if father_alive else 'they considered her a Jewish commie'

        story += f" I was {self.age1940} when Germany invaded The Netherlands. My {parent} had seen what was " + \
                 f"coming and shipped me off to England January that year. It is there that they told me {parent_pronoun} " + \
                 f"was executed in the second week of occupation. They {circumstance}."
        
        return story


    def output_child(self):
        self.backstory = self.backstory.replace('\n', '')
        self.backstory = self.backstory.replace('             ', ' ')
        child = {
            'name' : f'{self.name} {self.surname}',
            'age at move' : self.age1940, 
            'known traits' : self.known_traits,
            'all traits' : self.my_traits,
            'country affinities' : self.country_affinities, 
            'backstory' : self.backstory,
            'trauma' : self.trauma
        }
        pprint.pprint(child, sort_dicts=False)

    def output_adult(self):
        pass


class Controller:
    def __init__(self, input_file='') -> None:
        pass


j = Juana()
