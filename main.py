from ast import literal_eval
import json
from random import random, randint, choice, seed, choices, uniform, shuffle
from pprint import pprint
from copy import copy

from characters import Juana, Jules, Ika, Robin, Daniel
from sources import traits, event_traits, adult_tags, guardians
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
        self.crushes = {}
        for c in self.cs.values():
            for r in self.cs.values():
                if r.name != c.name:
                    if r.age1940 in range(c.age1940 - 1, c.age1940 + 4):
                        chance = (c.relationships[r.name] / 100 + 1) * 0.3
                        if random() < chance:
                            c.give_crush(r.name)
                            self.crushes[c.name] = r.name
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
