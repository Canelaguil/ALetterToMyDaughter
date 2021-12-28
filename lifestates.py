from copy import copy
from random import random, randint, choice, seed, choices, uniform, shuffle
from sources import fem_first_en, fem_first_nl, male_first_en, male_first_nl, surnames_nl, surnames_en

class Person:
    def __init__(self, nationality, sex, name=None, surname=None) -> None:
        self.nationality = nationality
        self.sex = sex
        self.name = name if name else self.get_first_name()
        self.surname = surname if surname else self.get_surname()

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
            
    def __str__(self):
        return f"{self.name} {self.surname}"

class RomanceLife:
    def __init__(self, sexuality, sex, year, country='Australia') -> None:
        self.state = 'single'
        self.year = year
        self.country = country
        self.log = {}
        self.sexuality = sexuality
        self.sex = sex 

        self.primary_partner = None
        self.secondary_partner = None
        self.is_married = False
        self.partnership = False
        self.is_engaged = False
        self.ex_spouses = []
        self.ex_partners = []

        self.log_change()

    def transition(self): 
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

    def find_partner(self):
        if self.sex == 'f':
            if self.sexuality == 'straight':
                return Person(self.country, 'm')
            elif self.sexuality == 'gay':
                return Person(self.country, 'f')
            else:
                if random() < 0.7:
                    return Person(self.country, 'm')
                else:
                    return Person(self.country, 'f')
        else:
            if self.sexuality == 'straight':
                return Person(self.country, 'f')
            elif self.sexuality == 'gay':
                return Person(self.country, 'm')
            else:
                if random() < 0.7:
                    return Person(self.country, 'f')
                else:
                    return Person(self.country, 'm')

    def single(self):
        if random() < 0.35:
            self.state = 'in love'
            self.primary_partner = self.find_partner()
            self.log_change()

    def in_love(self):
        # if hetero romance
        if self.primary_partner.sex != self.sex:
            if random() < 0.3:
                self.state = 'engaged'
                self.is_engaged = True
                self.log_change()
            elif random() < 0.3: 
                self.state = 'single'
                self.primary_partner = None 
                self.log_change()
        # if gay romance
        else:
            if random() < 0.15:
                self.state = 'partnership'
                self.partnership = True
                self.log_change()
            elif random() < 0.3: 
                self.state = 'single'
                self.primary_partner = None 
                self.log_change()

    def engaged(self):
        if random() < 0.5:
            self.state = 'married'
            self.is_married = True
            self.log_change()

    def married(self):
        if random() < 0.05: 
            self.state = 'cheating'
            self.secondary_partner = self.find_partner()
            self.log_change()
        elif random() < 0.05: 
            self.state = 'single'
            self.ex_spouses.append(copy(self.primary_partner))
            self.primary_partner = None 
            self.log_change()

    def partners(self):
        if random() < 0.05: 
            self.state = 'cheating'
            self.secondary_partner = self.find_partner()
            self.log_change()
        elif random() < 0.1: 
            self.state = 'single'
            self.ex_partners.append(copy(self.primary_partner))
            self.primary_partner = None 
            self.log_change()

    def cheating(self):
        if self.is_married: 
            if random() < 0.2:
                self.state = 'single'
                self.ex_spouses.append(copy(self.primary_partner))
                self.primary_partner = None 
                self.secondary_partner = None
                self.log_change()
            elif random() < 0.2: 
                self.state = 'married'
                self.ex_spouses.append(copy(self.primary_partner))
                self.primary_partner = self.secondary_partner
                self.secondary_partner = None
                self.log_change()
            elif random() < 0.2: 
                self.state = 'married'
                self.secondary_partner = None 
                self.log_change()
        elif self.partnership:
            if random() < 0.5: 
                self.state = 'single'
                self.ex_partners.append(copy(self.primary_partner))
                self.primary_partner = None 
                self.secondary_partner = None
                self.log_change()
            elif random() < 0.2: 
                self.state = 'partnership'
                self.ex_partners.append(copy(self.primary_partner))
                self.primary_partner = self.secondary_partner
                self.secondary_partner = None
                self.log_change()
            elif random() < 0.2: 
                self.state = 'partnership'
                self.secondary_partner = None
                self.log_change()

    def log_change(self):
        if self.secondary_partner:
            sec = f', cheated on with {self.secondary_partner}'
        else:
            sec = ''
        if self.primary_partner: 
            prim = f': {self.primary_partner}'
        else: 
            prim = ''

        self.log[self.year] = f'{self.state} {prim}{sec}'

    def get_log(self):
        return self.log

class ProffesionalLife: 
    def __init__(self) -> None:
        self.state = ''