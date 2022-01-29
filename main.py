from ast import literal_eval
import json
from random import random, randint, choice, seed, choices, uniform, shuffle
from pprint import pprint
from copy import copy

from characters import Juana, Jules, Ika, Robin, Daniel
from sources import traits, adult_tags, guardians
from memories import Memory, ChildhoodMemories


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
        self.the_event()
        self.warden_life()
        self.teenage_progress()
        self.start_adulthood()

    def childhood_memories(self):
        cdb = ChildhoodMemories()
        self.init_crushes()
        
        for _ in range(27):
            m = cdb.get_random()
            if m == {}: # if no more memories left
                break 

            m_inited = self.init_childhood_memory(m)
            if m_inited == {}: # if memory not chosen
                continue 

            for child in self.cs.values(): 
                child.add_memory(m_inited, 'child')
        
        for child in self.cs.values(): 
            child.output_child()
    
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
        return m
            
    def init_crushes(self):
        self.crushes = {}
        for c in self.cs.values():
            for r in self.cs.values():
                if r.name != c.name:
                    if r.age1940 in range(c.age1940 - 1, c.age1940 + 5):
                        chance = (c.relationships[r.name] / 100 + 1) * 0.3
                        if random() < chance:
                            c.give_crush(r.name)
                            self.crushes[c.name] = r.name
                            break

    def the_event(self):
        # remove Daniel from character list
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
            for cname in self.cs:
                if cname not in event['involved'] and cname != 'Robin':
                    event['not_involved'].append(cname)
        
        # check how someone reacts
        event['reactions'] = {}
        for name, c in self.cs.items():
            event['reactions'][name] = c.interpret_event(event)
            c.output_event()

        # pprint(event)

        with open(f'objects/the_event.json', 'w') as outfile:
            json.dump(event, outfile, indent=2, sort_keys=False)

    def warden_life(self):
        global guardians
        for c in self.cs.values(): 
            if c.name == 'Robin': 
                c.give_guardian(guardians['nadia'])
                continue
            while True: 
                g = randint(1, 3)
                if guardians[g]['capacity'] != 0: 
                    guardians[g]['capacity'] -= 1
                    guardians[g]['ward'].append(c.name)
                    c.give_guardian(guardians[g])
                    break

    def teenage_progress(self):
        for c in self.cs.values(): 
            c.teenage_years()       

            # give sexuality
            if c.crush:
                other_sex = self.cs[c.crush].sex if c.crush != 'Daniel' else 'm'
                if other_sex == c.sex:
                    c.sexuality = choices(['bisexual', 'gay'], weights=[1, 3])[0]
                else: 
                    c.sexuality = choices(['bisexual', 'straight'], weights=[1, 3])[0]
            else:
                c.sexuality = choices(['bisexual', 'straight', 'gay'])[0]

            if c.name == 'Robin':
                c.sexuality == 'bisexual'
            c.output_teenager()

    def start_adulthood(self):
        self.cs.pop('Robin')
        for ch in self.cs.values():
            ch.become_adult()

        year = 1945
        
        while year < 1967:
            for ch in self.cs.values():
                ch.adult_year()
            year += 1

        for ch in self.cs.values():
            ch.output_adult()

Controller()
