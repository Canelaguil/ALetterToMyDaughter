from copy import copy
from random import random, randint, choice, seed, choices, uniform, shuffle
from sources import locations, allowance, lifestyle, fem_first_en, fem_first_nl, male_first_en, male_first_nl, surnames_nl, surnames_en

class Person:
    def __init__(self, nationality, sex, name=None, surname=None, age=0) -> None:
        self.nationality = nationality
        self.sex = sex
        self.alive = True
        self.name = name if name else self.get_first_name()
        self.surname = surname if surname else self.get_surname()
        self.get_age(age)

    def get_first_name(self): 
        if self.nationality == 'Netherlands':
            if self.sex == 'f':
                return choice(fem_first_nl)
            else: 
                return choice(male_first_nl)
        else:
            if self.sex == 'f':
                return choice(fem_first_en)
            else:
                return choice(male_first_en)

    def get_surname(self):
        if self.nationality == 'Netherlands':
            surname = choice(surnames_nl)
            # surnames_nl.remove(surname)
            return surname
        else:
            surname = choice(surnames_en)
            # surnames_en.remove(surname)
            return surname
            
    def get_age(self, age):
        if age > 0:
            low_range = age / 2 + 7 
            top_range = (age - 7) * 2
            self.age = randint(int(low_range), int(top_range))
            if self.age < 18:
                self.age = 18
        else:
            self.age = age

    def get_name(self):
       return f"{self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname} ({self.age})"

class RomanceLife:
    def __init__(self, sexuality, sex, year, country, traits, surname, tags, aspirations, people) -> None:
        self.state = 'single'
        self.traits = traits
        self.tags = tags
        self.aspirations = aspirations
        self.year = year
        self.surname = surname
        self.og_surname = surname
        self.age = 18
        self.country = country
        self.log = {}
        self.sexuality = sexuality
        self.sex = sex 

        self.primary_partner = None
        self.secondary_partner = None
        self.is_married = False
        self.partnership = False
        self.is_engaged = False
        self.people = people
        self.log_change()

    """
    TRANSITIONS 
    """
    def transition(self, location, tags): 
        self.country = location
        self.tags = tags
        if self.state == 'single':
            self.single()
        elif self.state == 'in love': 
            self.in_love()
        elif self.state == 'engaged':
            self.engaged()
        elif self.state == 'married': 
            self.married()
        elif self.state ==  'partnership':
            self.partners()
        elif self.state == 'cheating': 
            self.cheating()
        self.year += 1
        self.age += 1

        return self.is_married, self.tags, self.people

    def to_single(self):
        self.state = 'single'
        if not self.people['old_flame']:
            self.people['old_flame'] = self.primary_partner
        else:
            if random() < 0.5: 
                self.people['old_flame'] = self.primary_partner
        
        if self.sex == 'f': 
            self.surname = self.og_surname
            for ch in self.people['extra_marital_children']:
                ch.surname = self.og_surname
        self.primary_partner = None 
        self.secondary_partner = None
        self.is_married = False
        self.people['love_interest'] = None
        self.people['partner'] = None
        self.people['spouse'] = None
        self.people['affairpartner'] = None

        self.tags['married'] = False 
        self.tags['relationship'] = False
        self.log_change()

    def to_love(self):
        self.state = 'in love'
        self.primary_partner = self.find_partner()
        self.people['love_interest'] = self.primary_partner
        self.log_change()

    def to_engaged(self):
        self.state = 'engaged'
        self.is_engaged = True
        self.people['partner'] = self.primary_partner
        self.people['love_interest'] = None
        self.people['spouse'] = None
        self.people['affairpartner'] = None
        self.tags['relationship'] = True
        self.log_change()

    def to_married(self):
        self.state = 'married'
        self.is_married = True
        self.tags['married'] = True 
        self.tags['relationship'] = True
        self.people['love_interest'] = None
        self.people['partner'] = None
        self.people['spouse'] = self.primary_partner
        self.people['affairpartner'] = None
        self.secondary_partner = None
        if self.sex == 'm':
            self.primary_partner.surname = self.surname
        else:
            self.surname = self.primary_partner.surname
        self.log_change()

    def to_partners(self):
        self.state = 'partnership'
        self.partnership = True
        self.secondary_partner = None
        self.people['love_interest'] = None
        self.people['partner'] = self.primary_partner
        self.people['spouse'] = None
        self.people['affairpartner'] = None
        self.tags['relationship'] = True 
        self.log_change()

    def to_cheating(self):
        self.state = 'cheating'
        self.secondary_partner = self.find_partner()
        self.people['affairpartner'] = self.secondary_partner
        if random() < 0.5:
            self.tags['commitment-averse'] = True
        self.log_change()

    """
    STATES 
    """
    def single(self):
        tr_offset = 0.1 if 'daydreamer' in self.traits or 'trusting' in self.traits else 0
        if random() < (0.5 + tr_offset):
            self.to_love()

    def in_love(self):
        # if hetero romance
        if self.primary_partner.sex != self.sex:
            if random() < 0.4:
                self.to_engaged()
            elif random() < 0.4: 
                self.to_single()
        # if gay romance
        else:
            if random() < 0.25:
                self.to_partners()
            elif random() < 0.4: 
                self.to_single()

    def engaged(self):
        if random() < 0.5:
            self.to_married()

    def married(self):
        ch_chance = 0.2 if self.aspirations['children'] else -0.1
        if self.sex == 'f':
            if self.age < 35:
                if random() < (0.25 + ch_chance):
                    self.have_child()
        else:
            if self.primary_partner.age < 35:
                if random() < (0.25 + ch_chance):
                    self.have_child()

        ch_offset =  0.1 if self.tags['commitment-averse'] or 'jealous' in self.traits else 0
        if random() < (0.2 + ch_offset): 
            self.to_cheating()
        elif random() < 0.05: 
            if random() < 0.5:
                self.tags['divorced'] = True
            else:
                self.tags['widowed'] = True
                self.people['dead_partner'] = self.primary_partner
                self.primary_partner.alive = False
            
            self.people['ex_spouses'].append(copy(self.primary_partner))
            self.to_single()
        
    def partners(self):
        if self.aspirations['children']:
            if random() < 0.1:
                self.have_child('adopt')

        ch_offset =  0.1 if self.tags['commitment-averse'] or 'jealous' in self.traits else 0
        if random() < (0.03 + ch_offset): 
            self.to_cheating()
        elif random() < 0.07: 
            if random() < 0.5:
                self.tags['widowed'] = True
                self.people['dead_partner'] = self.primary_partner
                self.primary_partner.alive = False
            
            self.people['ex_partners'].append(copy(self.primary_partner))
            
    def cheating(self):
        # Possible child
        if self.sex == 'f' and self.secondary_partner.sex == 'm':
            if self.age < 35:
                if random() < 0.2:
                    self.have_child()
        elif self.sex == 'm' and self.secondary_partner.sex == 'f':
            if self.secondary_partner.age < 35:
                if random() < 0.35:
                    self.have_child()
        
        # If is married
        if self.is_married: 
            if random() < 0.2:
                self.people['ex_spouses'].append(copy(self.primary_partner))
                self.people['ex_partners'].append(copy(self.primary_partner))
                self.to_single()
            elif random() < 0.2: 
                self.people['ex_spouses'].append(copy(self.primary_partner))
                self.primary_partner = self.secondary_partner
                self.to_married()
            elif random() < 0.2: 
                self.to_married()
        # If relationship
        elif self.partnership:
            if random() < 0.5: 
                self.people['ex_partners'].append(copy(self.primary_partner))
                self.to_single()
            elif random() < 0.2: 
                self.people['ex_partners'].append(copy(self.primary_partner))
                self.primary_partner = self.secondary_partner
                self.to_partners()
            elif random() < 0.2: 
                self.to_partners()

    """
    HELP FUNCTIONS
    """
    def have_child(self, mode='bio'):
        self.tags['parent'] = True
        sex = choice(['f', 'm'])

        if mode == 'adopt':
            if random() < 0.6:
                sur = self.surname
            else:
                sur = None
        else:
            if self.sex == 'm':
                if self.state == 'married': 
                    sur = self.surname
                elif self.state == 'cheating':
                    sur = self.secondary_partner.surname
            else:
                if self.is_married:
                    sur = self.primary_partner.surname
                else:
                    sur = None
        child = Person(self.primary_partner.nationality, sex, age=0, surname=sur)
        if self.state == 'cheating':
            self.people['extra_marital_children'].append(child)
        else: 
            self.people['children'].append(child)

        self.log_change()

    def find_partner(self):
        if self.sex == 'f':
            if self.sexuality == 'straight':
                return Person(self.country, 'm', age=self.age)
            elif self.sexuality == 'gay':
                return Person(self.country, 'f', age=self.age)
            else:
                if random() < 0.7:
                    return Person(self.country, 'm', age=self.age)
                else:
                    return Person(self.country, 'f', age=self.age)
        else:
            if self.sexuality == 'straight':
                return Person(self.country, 'f', age=self.age)
            elif self.sexuality == 'gay':
                return Person(self.country, 'm', age=self.age)
            else:
                if random() < 0.7:
                    return Person(self.country, 'f', age=self.age)
                else:
                    return Person(self.country, 'm', age=self.age)

    def log_change(self):
        if self.secondary_partner:
            sec = f', cheated on with {self.secondary_partner}'
        else:
            sec = ''
        if self.primary_partner: 
            prim = f': {self.primary_partner}'
        else: 
            prim = ''
        if self.tags['parent']:
            children = ''
            for ch in self.people['children']:
                children += f"{ch}, "
            if self.people['extra_marital_children'] != []:
                children += 'and extra-marital children '
                for cx in self.people['extra_marital_children']:
                    children += f"{cx}, "
            chl = f", has children {children}"
        else: 
            chl = ''

        self.log[self.year] = f'{self.state}, age {self.age} {prim}{sec}{chl}'

    def get_log(self):
        return self.log

class ProfessionalLife: 
    def __init__(self, year, sex, aspirations, guardian, location, traits, people) -> None:
        self.year = year
        self.sex = sex
        self.traits = traits
        self.age = 18
        self.log = {}
        self.people = people
        self.guardian = guardian
        self.aspirations = aspirations
        self.location = location
        self.student_years = 0
        self.married = False
        self.is_student = False 
        self.was_student = False
        self.state = 'start'

    def transition(self, married, tags):
        self.tags = tags
        change = False
        if self.state == 'unemployed':
            change = self.unemployed()
        elif self.state == 'start':
            change = self.start()
        elif self.state == 'student':
            change = self.student()
        elif self.state == 'low job':
            change = self.low_job()
        elif self.state == 'medium job':
            change = self.medium_job()
        elif self.state == 'high job':
            change = self.high_job()
        elif self.state == 'very high job':
            change = self.very_high_job()

        if married != self.married:
            change = True
        
        self.married = married
        self.year += 1
        self.age += 1

        if change: 
            self.relocate()
            self.log_change()

        return self.location, self.tags, self.people

    def relocate(self):
        options = [self.location]
        if self.state == 'unemployed':
            pass
        elif self.state == 'student': 
            all_index = allowance.index(self.guardian['allowance'])
            if self.aspirations['location'] == 'Netherlands' and random() < (all_index * 0.2):
                self.location = locations[8]
            else: 
                options = filter(lambda x: x[2] == 'Australia' and x[3] == 'city', locations)
        elif self.state == 'high job' or self.state == 'very high job':
            if self.location[3] == 'city':
                if random() < 0.3:
                    options = filter(lambda x: x[2] == self.location[2] and x[3] == 'city', locations)
            else:
                options = filter(lambda x: x[2] == self.location[2] and x[3] == 'city', locations)
        else: 
            if self.location[2] != 'Netherlands' and self.aspirations['location'] == 'Netherlands':
                if random() < 0.4: 
                    options = filter(lambda x: x[2] == 'Netherlands', locations)
            elif self.location[2] != 'Australia' and self.aspirations['location'] == 'Australia':
                if random() < 0.4: 
                    options = filter(lambda x: x[2] == 'Australia', locations)            
            else: 
                if random() < 0.2:
                    options = filter(lambda x: x[2] == self.location[2], locations)
        ops = list(options)
        self.location = choice(ops)

    def start(self):
        self.lifestyle = self.guardian['lifestyle']
        self.income_class = self.guardian['income_class']
        self.location = self.guardian['location']

        if self.aspirations['college']:
            # If they want to study
            if self.sex == 'f':
                if self.guardian['provide_women_college']:
                    self.state = 'student'
                else:
                    if lifestyle.index(self.lifestyle) > 1:
                        self.state = 'unemployed'
                    else: 
                        self.state = 'low job'
            else:
                if self.guardian['provide_college']:
                    self.state = 'student'
                else:
                    if lifestyle.index(self.lifestyle) > 2:
                        if random() < 0.9:
                            self.state = 'medium job'
                        else:
                            self.state = 'low job'
                    else:
                        if random() < 0.8: 
                            self.state = 'low job'
                        else: 
                            self.state = 'medium job'
        # if no aspiration for college
        else: 
            if self.sex == 'f':
                if lifestyle.index(self.lifestyle) > 1:
                    self.state = 'unemployed'
                else: 
                    self.state = 'low job'
            else:
                if lifestyle.index(self.lifestyle) > 2:
                    if random() < 0.8:
                        self.state = 'medium job'
                    else:
                        self.state = 'low job'
                else:
                    if random() < 0.8: 
                        self.state = 'low job'
                    else: 
                        self.state = 'medium job'
        return True

    def student(self): 
        if self.student_years > 3: 
            # Chance of stopping study
            if random() < 0.7:
                if random() < 0.5: 
                    self.state = 'medium job'
                else:
                    self.state = 'high job'
                self.is_student = False
                self.was_student = True
                return True
        self.is_student = True
        self.student_years += 1
        return False

    def unemployed(self): 
        if self.sex == 'f':
            if lifestyle.index(self.lifestyle) > 1:
                self.state = 'unemployed'
                if not self.married:
                    # if ambitious
                    if self.aspirations['college']:
                        if random() < 0.6: 
                            self.state = 'low job'
                            return True
                    else:
                        if random() < 0.3: 
                            self.state = 'low job'
                            return True
                else: 
                    # if ambitious
                    if self.aspirations['college']:
                        if random() < 0.3: 
                            self.state = 'low job'
                            return True
                    else:
                        if random() < 0.005: 
                            self.state = 'low job'
                            return True

    def low_job(self):
        if self.sex == 'm':
            if random() < 0.1:
                self.state = 'medium job'
                return True
        else: 
            if random() < 0.05:
                self.state = 'medium job'
                return True
            if self.married:
                if random() < 0.5: 
                    self.state == 'unemployed'
                    return True
        return False

    def medium_job(self):
        if self.sex == 'm':
            if random() < 0.2: 
                self.state = 'high job'
                return True
        else:
            if random() < 0.1: 
                self.state = 'high job'
                return True
        return False

    def high_job(self):
        if self.sex == 'm':
            if random() < 0.075: 
                self.state = 'very high job'
                return True
        else:
            if random() < 0.025: 
                self.state = 'very high job'
                return True
        return False

    def very_high_job(self):
        return False

    def log_change(self):
        self.log[self.year] = f'{self.state}, age {self.age} in {self.location[0]}, {self.location[1]} ({self.location[2]}) with a {self.lifestyle} lifestyle while married {self.married}'

    def get_log(self):
        return self.log

class IOLife:
    def __init__(self, people, location, guardian, tags, year, sex) -> None:
        self.people = people     
        self.sex = sex
        self.location = location
        self.guardian = guardian
        self.year = year
        self.tags = tags
        self.age = 18
        self.init_people()

    def init_people(self):
        g = Person('Australia', self.guardian['sex'], self.guardian['name'], self.guardian['surname'])
        g.age = self.guardian['age'] + (self.year - 1945)
        self.people['guardian'] = g
        self.people['bestfriend'] = self.make_person()
        self.people['childhoodfriend'] = self.make_person()
        self.people['childhoodfriend'].age = self.age
        self.people['friend'] = self.make_person()


    def transition(self, people, location, tags):
        self.people = people
        if self.location != location: 
            self.location = location
            self.update_people()
        self.tags = tags
        self.update_ages()
        self.update_people()
        return self.people, self.tags

    def make_person(self, mode='pref_sex'): 
        """
        modes: 
        - random
        - pref_sex
        """
        if mode =='pref_sex':
            if self.sex == 'f':
                    sex = 'f' if random() < 0.7 else 'm'
            else: 
                sex = 'm' if random() < 0.7 else 'f'
        else: 
            sex = choice(['m', 'f'])

        return Person(self.location, sex, age=self.age)

    def update_people(self):
        for ch in ['friend', 'bfriend', 'enemy', 'familyfriend']: 
            if random() < 0.7:
                self.people[ch] = self.make_person()
            
        if random() < 0.3:
            self.people['bestfriend'] = self.make_person()

        if random() < 0.5: 
            self.people['pet'] = Person(self.location, self.sex, surname=' ')

    def update_ages(self):
        self.age += 1

        for key, p in self.people.items():
            if key == 'pet' and p:
                if p.age > 12:
                    if random() < 0.7:
                        p.alive = False 
                        self.people[key] = None
                        continue
            if p:
                if isinstance(p, list): 
                    for pp in p:
                        if pp.alive:
                            pp.age += 1
                else:
                    if p.alive:
                        p.age += 1

    def get_people(self):
        people = {}
        for key, value in self.people.items():
            if isinstance(value, list):
                strings = ""
                for p in value:
                    strings += f"{p.__str__()}, "
                people[key] = strings
            else:        
                people[key] = value.__str__()
        return people
