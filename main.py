from ast import literal_eval
import json
from random import random, randint, choice, seed, choices, uniform, shuffle
from pprint import pprint
from copy import copy

from numpy.lib.arraysetops import isin
from sources import traits, event_traits, adult_tags, guardians
from memories import Memory, ChildhoodMemories

class Character:
    def __init__(self):
        seed()
        self.guilt = 0
        self.relationships = {
            'Juana' : 0, 
            'Jules' : 0,
            'Ika' : 0,
            'Robin' : 0,
            'Daniel' : 0
        }
        self.childhood_memories = {}
        self.crush = None

    def set_up(self):
        # Get traits
        while len(self.my_traits) < 5:
            t1, t2 = choice(traits)
            if t1 not in self.my_traits and t2 not in self.my_traits:
                t = choice([t1, t2])
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
            if fm == 'Robin' or random() < 0.2:
                bonus = randint(5, 20)
                self.modify_relationship(bonus, fm)

    def interpret_event(self, event):
        self.age1945 = self.age1940 + 5
        dan_R = self.relationships['Daniel']
        self.reaction = {'age' : self.age1945}

        # GUILT
        if event['pusher'] == self.name:
            self.guilt += randint(dan_R, 100)
            if self.crush == 'Daniel':
                self.guilt += randint(20, 30)
                self.modify_trauma(randint(20, 50))

        elif self.name in event['involved']:
            self.guilt += randint(int(dan_R * 0.5), int(dan_R * 1.2))
            if self.crush == 'Daniel':
                self.guilt += randint(10, 20)
                self.modify_trauma(randint(10, 40))
        else:
            self.guilt += randint(0, dan_R)
        self.guilt = self.guilt if self.guilt < 100 else 100
        self.reaction['guilt'] = self.guilt

        # TRAUMA
        trauma_modifier = self.guilt * uniform(0.4, 0.8)
        self.reaction['trauma'] = {'old_trauma' : self.trauma}
        self.modify_trauma(trauma_modifier)
        self.reaction['trauma']['trauma_modifier'] = trauma_modifier
        self.reaction['trauma']['new_trauma'] = self.trauma

        # RELATIONSHIPS (TODO)
        self.relationships.pop('Daniel')
        self.reaction['relationships'] = {}
        for r in self.relationships:
            if r != 'Robin':
                self.reaction['relationships'][r] = {'old_R' : self.relationships[r]}
                m = randint(-30, 30)
                self.modify_relationship(m, r)
                self.reaction['relationships'][r]['new_R'] = self.relationships[r]

        return self.reaction

    def become_adult(self):
        self.tags = copy(adult_tags)

    """
      CHECK CHARACTER 
    """

    def has_trait(self, trait):
        return trait in self.my_traits

    """ 
      MODIFY CHARACTERS
    """

    def modify_relationship(self, modifier, name):
        cur_value = self.relationships[name] 
        new_value = cur_value + modifier
        if new_value > 100:
            new_value = 100
        elif new_value < 0:
            new_value = 0
        self.relationships[name] = new_value

    def modify_trauma(self, modifier):
        new_value = self.trauma + int(modifier)
        if new_value > 100:
            new_value = 100
        elif new_value < 0:
            new_value = 0
        self.trauma = new_value

    def give_crush(self, crush):
        self.crush = crush

    def add_memory(self, memory, category='adult'):
        if category == 'adult':
            self.memory.add_memory(memory)
        else:
            self.memory.add_childhood_memory(memory)

    """
      OUTPUT FUNCTIONS
    """

    def output_child(self):
        self.backstory = self.backstory.replace('\n', '')
        self.backstory = self.backstory.replace('             ', ' ')
        child = {
            'name' : f'{self.name} {self.surname}',
            'age at move' : self.age1940, 
            'known traits' : self.known_traits,
            'all traits' : self.my_traits,
            'country affinities' : self.country_affinities, 
            'relationships' : self.relationships,
            'memory' : self.memory.get_memory(),
            'backstory' : self.backstory,
            'trauma' : self.trauma,
            'crush' : self.crush
        }
        self.write_json(child, 'child')

    def output_event(self):
        child = {
            'name' : f'{self.name} {self.surname}',
            'age at event' : self.age1945, 
            'known traits' : self.known_traits,
            'all traits' : self.my_traits,
            'country affinities' : self.country_affinities, 
            "relationships" : self.relationships,
            'trauma' : self.trauma, 
            'reaction' : self.reaction,
            'crush' : self.crush
        }
        self.write_json(child, 'event')

    def output_adult(self):
        adult = {
            'name' : f'{self.name} {self.surname}',
            'age at event' : self.age1945 + 21, 
            'known traits' : self.known_traits,
            'all traits' : self.my_traits,
            'tags' : self.tags,
            'country affinities' : self.country_affinities, 
            "relationships" : self.relationships,
            'trauma' : self.trauma
        }
        self.write_json(adult, 'adult')

    def write_json(self, object, stage):
        # pprint(object)
        with open(f'objects/{self.name}_{stage}.json', 'w') as outfile:
            json.dump(object, outfile, indent=4, sort_keys=False)

    
class Juana(Character):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Juana"
        self.surname = "Huijzen"
        self.memory = Memory(self.name)
        self.known_traits = ['kind', 'moody']
        self.my_traits = ['kind', 'moody']
        self.trauma = randint(0, 50)
        self.country_affinities = {
            'Netherlands': 0, 'Spain': 0, 'Australia': 0}
        self.sex = 'f'
        self.age1940 = 13

        self.set_up()
        self.backstory = self.backstory()
        self.birth_year = 1940 - self.age1940

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
        self.memory = Memory(self.name)
        self.known_traits = ['impulsive', 'creative']
        self.my_traits = ['impulsive', 'creative']
        self.trauma = randint(20, 60)
        self.country_affinities = {
            'Netherlands': -2, 'Belgium': -1, 'Australia': -1}
        self.sex = 'm'
        self.age1940 = 13

        self.set_up()
        self.backstory = self.backstory()
        self.birth_year = 1940 - self.age1940

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

        story += f"When Germany invaded the Netherlands I was {self.age1940}. My parents had send me " + \
                 " to England days prior. I never saw them again."
        
        return story


class Ika(Character):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Ika"
        self.surname = "Nicolaas"
        self.memory = Memory(self.name)
        self.known_traits = ['brave', 'outgoing']
        self.my_traits = ['brave', 'outgoing']
        self.trauma = randint(0, 20)
        self.country_affinities = {
            'Netherlands': 0, 'Indonesia': 0, 'Australia': 0}
        self.sex = 'f'
        self.age1940 = 12

        self.set_up()
        self.backstory = self.backstory()
        self.birth_year = 1940 - self.age1940

    def backstory(self):
        self.back_snippets = {
            'mother' :  "I found out she was murdered for her collaboration with the resistance.", 
            'father' : "I don't know where my father is now. He was a student in Amsterdam, but he was forced to go " + \
                       "back to Indonesia when they found out about me."
        }
        story = "My mother was Dutch, but she was as un-Dutch as one can be. People there love to say " + \
                "just act normal, that's strange enough, but normal was never strange enough for her. " + \
                "Just imagine: this good protestant girl from Veenendaal running away to Amsterdam: " + \
                "she was barely 15. And yet she survived. Became a bartender, took odd jobs wherever she could, " + \
                "and when my father was forced to go back to Indonesia she raised me on her own. " + \
                "When the war loomed on the horizon she became too involved in her political causes to look " + \
                f"after me. I was {self.age1940} when she send me away."
      
        return story


class Robin(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Robin'
        self.surname = 'Kuijper'
        self.memory = Memory(self.name)
        self.age1940 = 7
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
        self.sex = 'm'
        self.age1945 = self.age1940 + 5
        self.birth_year = 1940 - self.age1940

    def interpret_event(self, event):
        self.reaction = "Not present"
        return self.reaction


class Daniel(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Daniel'
        self.surname = 'de Bruijn'
        self.memory = Memory(self.name)
        self.age1940 = randint(12, 14)
        self.known_traits = ['creative', 'outgoing']
        self.my_traits = ['creative', 'outgoing', 'mean', 'impulsive', 'insecure']
        self.all_traits = [] 
        self.backstory = "Mother died in childbirth. Father was part of the socialist party, saw what was " + \
                         "coming and moved to England. Was drafted for war and died in 1939, leaving Daniel " + \
                         "orphaned."
        self.trauma = randint(0, 20)
        self.country_affinities = {
            'Netherlands': 2, 'Australia': 2 }        
        self.relationships = {
            'Juana' : randint(30, 80), 
            'Jules' : randint(30, 80),
            'Ika' : randint(30, 80),
            'Robin' : randint(60, 90)
        }
        self.sex = 'm'
        self.age1945 = self.age1940 + 5
        self.birth_year = 1940 - self.age1940

    def interpret_event(self, event):
        self.reaction = ""
        return self.reaction


class Controller:
    def __init__(self) -> None:
        self.cs = {
            'Juana' : Juana(),
            'Jules' : Jules(),
            'Ika' : Ika(),
            'Robin' : Robin(),
            'Daniel' : Daniel()
        }

        self.childhood_memories()

        for child in self.cs.values(): 
            child.output_child()
            
        self.the_event()

    def childhood_memories(self):
        self.cdb = ChildhoodMemories()
        self.init_crushes()
        
        for _ in range(27):
            m = self.cdb.get_random()
            if m == {}: # if no more memories left
                break 

            m_inited = self.init_childhood_memory(m)
            if m_inited == {}: # if memory not chosen
                continue 

            for child in self.cs.values(): 
                child.add_memory(m_inited, 'child')
    
    def init_childhood_memory(self, m):
        chances = {}
        names = {
            'me' : '', 
            'name1' : '', 
            'name2' : '',
            'name3' : '', 
            'name4' : ''
        }

        # Determine chance of event for each character
        for name, ch in self.cs.items():
            c = m['base_chance']
            ch_increase = literal_eval(m['ch_increase'])
            ch_decrease = literal_eval(m['ch_decrease'])
            if ch_increase != None:
                for tr in ch_increase:
                    if ch.has_trait(tr):
                        c *= 1.5
            if ch_decrease:
                for tr in ch_decrease:
                    if ch.has_trait(tr):
                        c *= 0.5
            chances[name] = c
        # print(chances)
            
        # Go over all names in random order and match event
        items = list(chances.items())
        shuffle(items)
        found_me = False
        for n, p in items: 
            if random() < p: 
                found_me = True
                names['me'] = n
                m['people'] = literal_eval(m['people'])
                for i in m['people']:
                    while True: 
                        rn = choice(items)
                        if rn[0] not in names.values():
                            names[i] = rn[0]
                            break
                break
        if not found_me:
            return {}

        m['mapping'] = names
        m['description'] = m['description'].replace('{me}', names['me'])
        m['description'] = m['description'].replace('{name1}', names['name1'])
        m['description'] = m['description'].replace('{name2}', names['name2'])
        m['description'] = m['description'].replace('{name3}', names['name3'])
        m['description'] = m['description'].replace('{name4}', names['name4'])
        # print(m['description'])
        return m
            
    def init_crushes(self):
        for c in self.cs.values():
            for r in self.cs.values():
                if r.name != c.name:
                    if r.age1940 in range(c.age1940 - 1, c.age1940 + 4):
                        chance = (c.relationships[r.name] / 100 + 1) * 0.3
                        # print(chance)
                        if random() < chance:
                            c.give_crush(r.name)
                            # print(f'{c.name} has a crush on {r.name}')
                            break
    
    def the_event(self):
        self.cs.pop('Daniel')
        event = {}
        causes = [
            "Daniel is a bully",
            "Daniel mocked Ika's parents", 
            "Daniel is lying about Jules' parents", 
            "Daniel insulted Juana's parents",
            "Daniel is too bossy", 
            "Daniel lied to their caretaker",
            "Daniel was mean to Robin"
            ]
        event['cause'] = choice(causes)

        # find fighter
        choice_list = [
            (c.name, 100 - c.relationships['Daniel'])
            for c in self.cs.values() if c.name != 'Robin']
        a, w = zip(*choice_list)
        fighter = choices(a, weights=w)[0]
        event['fighter'] = fighter

        # find pusher
        choice_list = [
            (c.name, 100 - c.relationships['Daniel'] + c.relationships[fighter]) 
            for c in self.cs.values() if c.name not in ['Robin', fighter]]
        a, w = zip(*choice_list)
        pusher = choices(a, weights=w, k=2)
        event['pusher'] = pusher[0]

        # check if others were also involved
        event['involved'] = [fighter, pusher[0]]
        event['not_involved'] = []
        if random() < 0.5:
            if pusher[1]  not in event['involved']:
                event['involved'].append(pusher[1])
        else:
            for c in self.cs:
                if c not in event['involved'] and c != 'Robin':
                    event['not_involved'].append(c)
        
        # check how someone reacts
        event['reactions'] = {}
        for name, c in self.cs.items():
            event['reactions'][name] = c.interpret_event(event)
            c.output_event()

        pprint(event)

        with open(f'objects/the_event.json', 'w') as outfile:
            json.dump(event, outfile, indent=2, sort_keys=False)


Controller()
