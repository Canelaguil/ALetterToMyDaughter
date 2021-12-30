from copy import copy
from random import random, randint, choice, seed, choices, uniform, shuffle
from sources import locations, allowance, lifestyle, fem_first_en, fem_first_nl, male_first_en, male_first_nl, surnames_nl, surnames_en

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
        self.age += 1

        return self.is_married

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
        if random() < 0.4:
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
            elif random() < 0.4: 
                self.state = 'single'
                self.primary_partner = None 
                self.log_change()
        # if gay romance
        else:
            if random() < 0.15:
                self.state = 'partnership'
                self.partnership = True
                self.log_change()
            elif random() < 0.4: 
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
            self.is_married = False
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
                self.is_married = False
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

        self.log[self.year] = f'{self.state}, age {self.age} {prim}{sec}'

    def get_log(self):
        return self.log

class ProfessionalLife: 
    def __init__(self, year, sex, aspirations, guardian, location) -> None:
        self.year = year
        self.sex = sex
        self.age = 18
        self.log = {}
        self.guardian = guardian
        self.aspirations = aspirations
        self.location = location
        self.student_years = 0
        self.married = False
        self.is_student = False 
        self.was_student = False
        self.state = 'start'

    def transition(self, married):
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

        return self.location

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

        
        