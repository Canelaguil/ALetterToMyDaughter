import json
from random import random, randint, choice, seed, choices
from pprint import pprint

traits = ['apathetic', 'disorganised', 'anxious', 'critical', 'quirky',
          'egocentric', 'creative', 'moral', 'impulsive', 'happy', 'obedient', 'brave']


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


class Character:
    def __init__(self):
        seed()
        self.guilt = 0
        self.relationships = {
            'Juana' : 0, 
            'Jules' : 0,
            'Ika' : 0,
            'Benjamin' : 0,
            'Daniel' : 0
        }

    def set_up(self):
        # Get traits
        while len(self.my_traits) < 5:
            t = choice(traits)
            if t not in self.my_traits:
                self.my_traits.append(t)

        # Country affinities
        for country in self.country_affinities:
            self.country_affinities[country] += randint(-3, 3)
            if self.country_affinities[country] > 3: 
                self.country_affinities[country] = 3
            elif self.country_affinities[country] < -3: 
                self.country_affinities[country] = -3

        # Init relationships
        self.relationships.pop(self.name)
        for fm in self.relationships:
            m = randint(40, 80)
            self.modify_relationship(m, fm)
            if fm == 'Benjamin' or random() < 0.2:
                bonus = randint(5, 20)
                self.modify_relationship(bonus, fm)


    def modify_relationship(self, modifier, name):
        cur_value = self.relationships[name] 
        new_value = cur_value + modifier
        if new_value > 100:
            new_value = 100
        elif new_value < 0:
            new_value = 0
        self.relationships[name] = new_value

    def interpret_event(self, event):
        if event['pusher'] == self.name:
            self.guilt += randint(40, 100)
        else:
            pass


    def output_child(self):
        self.backstory = self.backstory.replace('\n', '')
        self.backstory = self.backstory.replace('             ', ' ')
        child = {
            'name' : f'{self.name} {self.surname}',
            'age at move' : self.age1940, 
            'known traits' : self.known_traits,
            'all traits' : self.my_traits,
            'country affinities' : self.country_affinities, 
            "relationships" : self.relationships,
            'backstory' : self.backstory,
            'trauma' : self.trauma
        }
        pprint(child, sort_dicts=False)
        self.write_json(child, 'child')

    def post_event_output(self):
        child = {
            'name' : f'{self.name} {self.surname}',
            'age at move' : self.age1940, 
            'known traits' : self.known_traits,
            'all traits' : self.my_traits,
            'country affinities' : self.country_affinities, 
            "relationships" : self.relationships,
            'trauma' : self.trauma
        }
        pprint(child, sort_dicts=False)
        self.write_json(child, 'post-event')

    def write_json(self, object, stage):
        with open(f'objects/{self.name}_{stage}.json', 'a') as outfile:
            json.dump(object, outfile, indent=2)

    def output_adult(self):
        pass


class Juana(Character):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Juana"
        self.surname = "Huijzen"
        self.known_traits = ['kind', 'moody']
        self.my_traits = ['kind', 'moody']
        self.trauma = randint(0, 50)
        self.country_affinities = {
            'Netherlands': 0, 'Spain': 0, 'Australia': 0}
        self.set_up()
        self.backstory = self.backstory()

    def backstory(self):
        father_alive = True
        story = "I was born in Spain, where my parents met while fighting for the Spanish " + \
                "civil war. " 
        
        if random() < 0.5: 
            story += "My mother was a fervent communist, one of the leaders of " + \
                     "The Cause. My father had travelled there all the way from the Netherlands. But "
        else:
            story += "My mother was a victim of class and circumstance. She hardly knew how to read, " + \
                     "she was a communist because everyone else she knew was. My father on the other hand " + \
                     "had come all the way from the Netherlands to fight for the cause. But "

        if random() < 0.5:
            story += "he never came back. Right before  the communists lost, my mother packed " + \
                     "up and took me to the Netherlands. She didn't even speak the language. " + \
                     "Her dark, Spanish features got us mistaken for Jews."

            father_alive = False 
            self.trauma += randint(0, 20)
            self.country_affinities['Spain'] = min(self.country_affinities['Spain'] + 2, 3)
            self.country_affinities['Netherlands'] = max(self.country_affinities['Netherlands'] - 2, -3)
        else:
            story += "in the war he lost my mother and with her his faith in the cause and " + \
                     "humanity at large. He took me back to the Netherlands." 
            self.country_affinities['Netherlands'] = min(self.country_affinities['Netherlands'] + 2, 3)

        self.age1940 = randint(9, 14)
        parent = 'father' if father_alive else 'mother'
        parent_pronoun = 'he' if father_alive else 'she'
        circumstance = 'knew he was a communist' if father_alive else 'considered her a Jewish commie'

        story += f" I was {self.age1940} when Germany invaded The Netherlands. My {parent} had seen what was " + \
                 f"coming and shipped me off to England January that year. It is there that they told me {parent_pronoun} " + \
                 f"was executed in the second week of occupation. They {circumstance}."
        
        return story


class Jules(Character):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Jules"
        self.surname = "Cohen"
        self.known_traits = ['impulsive', 'creative']
        self.my_traits = ['impulsive', 'creative']
        self.trauma = randint(20, 60)
        self.country_affinities = {
            'Netherlands': -2, 'Belgium': -1, 'Australia': -1}
        self.set_up()
        self.backstory = self.backstory()

    def backstory(self):
        moveage = randint(1, 5)
        circumstance = choice(['thought it would be saver for us', 'got a job', 'liked it'])
        story = f"I came to the Netherlands when I was {moveage} years old. My father {circumstance} there. "
        
        if random() < 0.5: 
            story += "He was a true European. Spoke 4 languages, made himself understood in many more. " + \
                     "Europe never loved him back enough. Met my mother in a theatre in Brussels, I guess " + \
                     "they made do well enough. "
        else:
            story += "He was born in France, spend time in Berlin, Koningsberg before it got bad. " + \
                     "He met my mother in Brussels. My mother was an silent movie actress, but after " + \
                     "the switch to talkies finding work became hard for her in more ways than one. "

        self.age1940 = randint(10, 15)

        story += f"When Germany invaded the Netherlands I was {self.age1940}. My parents had send me " + \
                 " to England days prior. I never saw them again."
        
        return story


class Ika(Character):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Ika"
        self.surname = "Nicolaas"
        self.known_traits = ['brave', 'outgoing']
        self.my_traits = ['brave', 'outgoing']
        self.trauma = randint(0, 20)
        self.country_affinities = {
            'Netherlands': 0, 'Indonesia': 0, 'Australia': 0}
        self.set_up()
        self.backstory = self.backstory()

    def backstory(self):
        self.back_snippets = {
            'mother' :  "I found out she was murdered for her collaboration with the resistance.", 
            'father' : "I don't know where my father is now. He was a student in Amsterdam, but he was forced to go " + \
                       "back to Indonesia when they found out about me."
        }
        self.age1940 = randint(9, 15)
        story = "My mother was Dutch, but she was as un-Dutch as one can be. People there love to say " + \
                "just act normal, that's strange enough, but normal was never strange enough for her. " + \
                "Just imagine: this good protestant girl from Veenendaal running away to Amsterdam: " + \
                "she was barely 15. And yet she survived. Became a bartender, took odd jobs wherever she could, " + \
                "and when my father was forced to go back to Indonesia she raised me on her own. " + \
                "When the war loomed on the horizon she became too involved in her political causes to look " + \
                f"after me. I was {self.age1940} when she send me away."
      
        return story


class Benjamin(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Benjamin'
        self.surname = 'Kuijper'
        self.age1940 = 6
        self.known_traits = []
        self.my_traits = []
        self.all_traits = [] 
        self.backstory = ""
        self.trauma = randint(0, 20)
        self.country_affinities = {
            'Netherlands': 2, 'Australia': 3 }        
        self.relationships = {
            'Juana' : 80, 
            'Jules' : 80,
            'Ika' : 80,
            'Daniel' : 80
        }


class Controller:
    def __init__(self) -> None:
        self.cs = {
            'Juana' : Juana(),
            'Jules' : Jules(),
            'Ika' : Ika(),
            'Benjamin' : Benjamin()
        }

        for child in self.cs.values(): 
            child.output_child()

        self.the_event()

    def the_event(self):
        event = {}
        causes = ["Daniel is a bully", "Daniel is lying about Ika's parents", "Daniel is lying about Jules' parents", "Daniel is too bossy", "Daniel lied to their caretaker"]
        event['cause'] = choice(causes)

        # find fighter
        choice_list = [(c.name, 100 - c.relationships['Daniel']) for c in self.cs.values() if c.name != 'Benjamin']
        a, w = zip(*choice_list)
        fighter = choices(a, weights=w)[0]
        event['fighter'] = fighter

        # find pusher
        choice_list = [(c.name, 100 - c.relationships['Daniel'] + c.relationships[fighter]) for c in self.cs.values() if c.name not in ['Benjamin', fighter]]
        a, w = zip(*choice_list)
        pusher = choices(a, weights=w, k=2)
        event['pusher'] = pusher[0]

        # check if others were also involved
        event['involved'] = [fighter, pusher[0]]
        event['not_involved'] = []
        if random() < 0.5:
            event['involved'].append(pusher[1])
        else:
            for c in self.cs:
                if c != fighter and c != pusher[0] and c != 'Benjamin':
                    event['not_involved'].append(c)

        for c in self.cs.values():
            c.interpret_event(event)
        pprint(event, sort_dicts=False)

Controller()

