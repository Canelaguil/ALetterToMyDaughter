import json
from random import random, randint, choice, seed, choices, uniform, shuffle
from pprint import pprint
from copy import copy

from sources import traits, event_traits, adult_tags, guardians, lifestyle, income
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
            self.modify_country_affinity(country, randint(-3, 3))

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
        self.age = 18

    """
      CHECK CHARACTER 
    """

    def has_trait(self, trait):
        return trait in self.my_traits

    """ 
      MODIFY CHARACTERS
    """

    def modify_relationship(self, modifier, name):
        if not name in self.relationships: 
            self.relationships[name] = 0
        cur_value = self.relationships[name] 
        new_value = cur_value + modifier
        if new_value > 100:
            new_value = 100
        elif new_value < 0:
            new_value = 0
        self.relationships[name] = new_value

    def modify_trauma(self, modifier, set=False):
        if set: 
            self.trauma = modifier
            return
        new_value = self.trauma + int(modifier)
        if new_value > 100:
            new_value = 100
        elif new_value < 0:
            new_value = 0
        self.trauma = new_value

    def modify_country_affinity(self, country, modifier): 
        self.country_affinities[country] += modifier
        if self.country_affinities[country] < - 3: 
            self.country_affinities[country] = -3
        elif self.country_affinities[country] > 3: 
            self.country_affinities[country] = 3

    def add_memory(self, memory, category='adult'):
        if category == 'adult':
            self.memory.add_memory(memory)
        else:
            changes = self.memory.add_childhood_memory(memory)
            self.process_changes(changes)

    def process_changes(self, changes): 
        # change relationships
        for p, v in changes['relationships'].items():
            self.modify_relationship(v, p)

    """ 
      MEMORY STUFF
    """

    def give_crush(self, crush):
        self.crush = crush
        memory = {
                "description": f"I had a crush on {crush}",
                "category": "childhood",
                "keyword": "crush",
                "people": [self.name, crush],
                "memory_relation_impact": "positive"
            }
        self.memory.add_pre_config_childhood_memory(memory, crush)
        changes = {
            'relationships' : {
                crush : randint(10, 30)
            }
        }
        self.process_changes(changes)

    def give_guardian(self, guardian): 
        guardian_name = f"{guardian['name']} {guardian['surname']}"
        self.person_tags = {}
        self.person_tags['guardian'] = guardian_name
        self.guardian = guardian 

        g_R = randint(10, 50)
        if self.guardian['nurturing']: 
            g_R += randint(20, 60)
        if self.guardian['provide_boarding_school']: 
            g_R -= randint(10, 40)
        if self.guardian['other_children']: 
            g_R += randint(-20, 20)
        
        self.modify_relationship(g_R, guardian_name)
        self.location = guardian['location']
        self.lifestyle = guardian['lifestyle']
        self.income_class = guardian['income_class']
        self.modify_country_affinity('Australia', int(g_R / 100 * 3))

    def teenage_years(self): 
        # trauma
        t_years = 18 - self.age1945
        g_R = self.relationships[self.person_tags['guardian']]
        guardian_factor = int(-1 * g_R / 10)
        guardian_factor = -3 if guardian_factor > -3 else guardian_factor
        new_trauma = self.trauma + guardian_factor * t_years
        new_trauma = int(0.1 * self.trauma) if new_trauma < 0 else new_trauma
        self.modify_trauma(new_trauma, True)

        # aspirations
        l_index = randint(lifestyle.index(self.lifestyle), len(lifestyle) - 1)
        i_index = randint(income.index(self.income_class), len(income) -1)
        c_chance = 0.5
        if 'curious' in self.my_traits or 'intelligent' in self.my_traits or 'ambitious' in self.my_traits: 
            c_chance += 0.2
        if 'disinterested' in self.my_traits or 'unambitious' in self.my_traits or 'slow' in self.my_traits:
            c_chance -= 0.2
        self.aspirations = {
            'lifestyle' : lifestyle[l_index], 
            'income' : income[i_index], 
            'children' : False if random() < self.trauma / 100 else True,
            'location' : max(self.country_affinities, key=self.country_affinities.get),
            'college' : True if random() < c_chance else False
        }

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

    def output_teenager(self): 
        child = {
            'name' : f'{self.name} {self.surname}',
            'age' : 18, 
            'known traits' : self.known_traits,
            'all traits' : self.my_traits,
            'guardian' : self.guardian,
            'location' : self.location, 
            'lifestyle' : self.lifestyle, 
            'income class' : self.income_class, 
            'boarding school' : self.guardian['provide_boarding_school'],
            'country affinities' : self.country_affinities, 
            "relationships" : self.relationships,
            'person tags' : self.person_tags, 
            'trauma' : self.trauma, 
            'aspirations' : self.aspirations, 
        }
        self.write_json(child, 'teenager')

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
        self.age1940 = 9

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
            self.modify_country_affinity('Spain', 2)
            self.modify_country_affinity('Netherlands', -2)
        else:
            story += "in the war he lost my mother and with her his faith in the cause and " + \
                     "humanity at large. He took me back to the Netherlands." 
            self.modify_country_affinity('Netherlands', 2)

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
        self.age1940 = 9

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
        self.age1940 = 8

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
        self.age1940 = 5
        self.known_traits = []
        self.my_traits = []
        self.all_traits = [] 
        self.backstory = ""
        self.trauma = randint(0, 20)
        self.country_affinities = {
            'Netherlands': 2, 'Australia': 3 }        
        self.relationships = {
            'Juana' : randint(70, 90), 
            'Jules' : randint(70, 90), 
            'Ika' : randint(70, 90), 
            'Daniel' : randint(70, 90), 
        }
        self.sex = 'x'
        self.age1945 = self.age1940 + 5
        self.birth_year = 1940 - self.age1940
        # self.give_crush(max(self.relationships, key=self.relationships.get))

    def interpret_event(self, event):
        rD = self.relationships['Daniel']
        mt = randint(int(rD * 0.3),  int(rD * 0.8))
        self.reaction = { 
            'age' : self.age1945,
            'old_trauma' : self.trauma, 
            'trauma_modifier' : mt, 
            }
        self.modify_trauma(mt)
        self.reaction['new_trauma'] = self.trauma
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
