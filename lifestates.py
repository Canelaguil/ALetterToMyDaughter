from copy import copy
from random import random, randint, choice, seed, choices, uniform, shuffle
from sources import locations, allowance, lifestyle, fem_first_en, fem_first_nl
from sources import male_first_en, male_first_nl, surnames_nl, surnames_en
from sources import male_jobs, fem_jobs, income, lifestyle

class Person:
    def __init__(self, nationality, sex, name=None, surname=None, age=0, title=None) -> None:
        self.nationality = nationality
        self.title = title
        self.sex = sex
        self.alive = True
        self.name = name if name else self._get_first_name()
        self.surname = surname if surname else self._get_surname()
        self._get_age(age)

    def _get_first_name(self): 
        if self.title:
            if self.title ==  'child':
                if self.sex == 'f': 
                    self.title = 'daughter'
                else: 
                    self.title = 'son'
            elif self.title == 'spouse':
                if self.sex == 'f':
                    self.title = 'wife'
                else:
                    self.title = 'husband'
        
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

    def _get_surname(self):
        if self.nationality == 'Netherlands':
            surname = choice(surnames_nl)
            # surnames_nl.remove(surname)
            return surname
        else:
            surname = choice(surnames_en)
            # surnames_en.remove(surname)
            return surname
      
    def _get_age(self, age):
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
    def __init__(self, sexuality, sex, country, traits, surname, tags, aspirations, people, age1945) -> None:
        self.state = 'single'
        self.traits = traits
        self.tags = tags
        self.aspirations = aspirations
        self.year = 1945
        self.surname = surname
        self.og_surname = surname
        self.age = age1945
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
        if self.age > 17:
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
        self.tags['abusive relationship'] = False
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
        self.tags['independent'] = True
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

        child = Person(self.primary_partner.nationality, sex, age=0, surname=sur, title='child')
        if self.state == 'cheating':
            self.people['extra_marital_children'].append(child)
        else: 
            self.people['children'].append(child)

        self.log_change()

    def find_partner(self, mode='partner'):
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
                return Person(self.country, 'f', age=self.age, title=mode)
            elif self.sexuality == 'gay':
                return Person(self.country, 'm', age=self.age, title=mode)
            else:
                if random() < 0.7:
                    return Person(self.country, 'f', age=self.age, title=mode)
                else:
                    return Person(self.country, 'm', age=self.age, title=mode)

    def log_change(self):
        log = {
            'age' : self.age,
            'state' : self.state,
            'married' : self.is_married
        }
        if self.primary_partner: 
            log['partner'] = self.primary_partner.__str__()

        if self.secondary_partner:
            log['cheating with'] = self.secondary_partner.__str__()


        if self.tags['parent']:
            children = ''
            if self.people['children'] != []:
                for ch in self.people['children']:
                    children += f"{ch}, "
                log['children'] = children

            xchildren = ''
            if self.people['extra_marital_children'] != []:
                for cx in self.people['extra_marital_children']:
                    xchildren += f"{cx}, "
                log['extra-marrital children'] = xchildren

        self.log[self.year] = log

    def get_log(self):
        return self.log


class ProfessionalLife: 
    def __init__(self, sex, aspirations, guardian, location, traits, people, age1945) -> None:
        self.year = 1945
        self.sex = sex
        self.traits = set(traits)
        self.age = age1945
        self.log, self.tags = {}, {}
        self.people = people
        self.guardian = guardian
        self.aspirations = aspirations
        self.location = location
        self.student_years = 0
        self.married = False
        self.is_student = False 
        self.was_student = False
        self.mobile = False
        self.state = 'start'
        self.income = None
        self.lifestyle = None
        self.job = None
        self.career = None

        self.creative_traits = {'quirky', 'unambitious', 'daydreamer', 'creative', 'exuberant', 'melancholic', 'optimistic'}
        self.rebellious_traits = {'rebellious', 'critical', 'creative', 'impulsive', 'daydreamer', 'optimistic'}
        self.ambitious_traits = {'intelligent', 'ambitious', 'optimistic', 'organised', 'workaholic', 'brave', 'confident'}
        self.unambitious_traits = {'lazy', 'unambitious', 'disinterested' , 'clumsy', 'nervous'}

    def transition(self, married, tags, traits):
        if self.age > 17:
            # recalculate  bonus assignment
            self.ambition_bonus = len(self.traits & self.ambitious_traits) * 0.05
            self.unambitious_bonus = len(self.traits & self.unambitious_traits) * 0.05

            self.tags = tags
            self.traits = set(traits)
            change = False
            if self.state == 'unemployed':
                change = self.unemployed()
            elif self.state == 'stay at home':
                change = self.stay_at_home()
            elif self.state == 'start':
                change = self.start()
            elif self.state == 'creative':
                change = self.creative()
            elif self.state == 'student':
                change = self.student()
            elif self.state == 'jailed': 
                change = self.jailed()
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

            if change: 
                self.change()

        self.year += 1
        self.age += 1

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
        elif self.state == 'high job' or self.state == 'very high job' or self.income > 1:
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
        new_location = choice(ops)
        if self.location != new_location: 
            self.location = new_location
            return True 
        else: 
            return False

    def change(self): 
        relocated = self.relocate()
        if self.state == 'unemployed' or self.state == 'stay at home' or self.state == 'student' or self.state == 'jailed':
            self.people['boss'] = None
            self.people['colleague'] = None 
        else: 
            self.people['boss'] = self.get_colleague()
            if relocated: 
                self.people['colleague'] = self.get_colleague()
            else: 
                if random() < 0.4: 
                    self.people['colleague'] = self.get_colleague()

        self.log_change()

    """
      CAREER START
    """
    def assign_career(self):

        # if woman
        if self.sex == 'f':
            self.female_career()
        # if man
        else: 
            self.male_career()

    def female_career(self):
        if random() < ((len(self.traits & self.creative_traits) + 0.1) / len(self.creative_traits)):
            creative_jobs = [job for job in fem_jobs if job[1] == 'creative']
            self.career = choice(creative_jobs)
            self.job = self.career[0]
            self.state = 'creative' 
            self.income = 0
            self.mobile = self.career[3]
            self.lifestyle = 0 if self.tags['independent'] else self.lifestyleS
            return
        else: 
            if self.lifestyle > 1:
                if random() < ((len(self.traits & self.rebellious_traits) + 0.1) / len(self.rebellious_traits)):
                    self.tags['independent'] = True
                    rebellious_jobs = [job for job in fem_jobs if job[2] == False and job[4] and job[1] != 'creative']
                    self.career = choice(rebellious_jobs)
                    self.lifestyle = lifestyle.index(self.career[1])
                else: 
                    proper_jobs = [job for job in fem_jobs if job[2] and job[4] and job[1] != 'creative']
                    self.career = choice(proper_jobs)
                    self.income = income.index(self.career[1])
                    self.lifestyle = lifestyle.index(self.career[1]) if self.tags['independent'] else self.lifestyle
            else: 
                if random() < ((len(self.traits & self.ambitious_traits) + 0.1) / len(self.ambitious_traits)): 
                    ambitious_jobs = [job for job in fem_jobs if job[1] == 'medium' and job[1] != 'creative']
                    self.career= choice(ambitious_jobs)
                else: 
                    random_jobs = [job for job in fem_jobs if job[1] != 'high' and job[1] != 'creative']
                    self.career = choice(random_jobs)
                self.lifestyle = lifestyle.index(self.career[1])
                self.tags['independent'] = True
            
            self.state = f"{self.career[1]} job"
            self.job = self.career[0]
            self.income = income.index(self.career[1])
            self.mobile = self.career[3]

    def male_career(self):
        if self.was_student:
            if random() < (0.7 + self.ambition_bonus): 
                jobs = [key for key, job in male_jobs.items() if job[2]]
            else: 
                jobs = [key for key, job in male_jobs.items() if job[3]]
            ladder = choice([0, 1])
        else: 
            if self.lifestyle > 1:
                if random() < ((len(self.traits & self.rebellious_traits) + 0.1) / len(self.rebellious_traits)):
                    jobs = [key for key, job in male_jobs.items() if not job[1] and job[3]]
                else: 
                    jobs = [key for key, job in male_jobs.items() if not job[1] and job[2]]
                ladder = choice([0, 1])
            else:
                ladder = 0
                jobs = [key for key, job in male_jobs.items() if job[3]]

        self.career = choice(jobs)
        self.job = male_jobs[self.career][0][ladder]
        if self.lifestyle > 1:
            self.lifestyle =  ladder + 1
        else: 
            self.lifestyle = ladder
        self.income = ladder
        self.state = f"{income[ladder]} job"

    def start(self):
        self.lifestyle = self.guardian['lifestyle']
        self.income = self.guardian['income_class']
        self.location = self.guardian['location']

        if self.sex == 'f':
            if self.lifestyle > 1:
                if self.aspirations['college'] and self.guardian['provide_women_college']:
                    self.state = 'student'
                    self.tags['independent'] = False
                else:
                    self.state = 'stay at home'
                    self.tags['independent'] = False
                    self.tags['with guardian'] = True
                    self.log_change()
                    return False
            else: 
                self.tags['independent'] = True
                self.assign_career()
        else:
            if self.aspirations['college'] and self.guardian['provide_college']:
                self.state = 'student'
                self.tags['independent'] = False
            else: 
                self.assign_career()
        return True

    """ 
      PHASES
    """
    def creative(self):
        self.creative_score = len(self.traits & self.creative_traits) 
        if random() < (self.creative_score * 0.005 + self.ambition_bonus): 
            if self.income < 4:
                self.income += 1 
            else:
                self.tags['famous'] = True 
            return True
        elif random() < 0.1: 
            if self.income == 0: 
                if self.tags['independent']:
                    self.state = 'unemployed'
                else: 
                    self.state = 'stay at home'
            else: 
                self.income -= 1
            return True
        
        if self.income > 0 and not self.tags['independent']:
            self.tags['independent'] = True 
            self.lifestyle = self.income
            return True
        return False
        
    def stay_at_home(self):
        if self.sex == 'f':
            if self.lifestyle > 1:
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

    def student(self): 
        if self.student_years > 3: 
            # Chance of stopping study
            if random() < 0.7:
                self.is_student = False
                self.was_student = True
                self.assign_career()
                return True
        self.is_student = True
        self.student_years += 1
        return False

    def unemployed(self): 
        if random() > self.trauma_modifier() * 2: 
            self.state = 'start'
        return False

    def jailed(self):
        self.tags['imprisoned'] = True
        self.tags['prev_imprisoned'] = True
        self.serving_time -= 1

        if self.serving_time == 0:
            self.tags['imprisoned'] = False
            if self.income != 0: 
                self.state = f"{income[self.income - 1]} job"
                self.income -= 1
                self.lifestyle -= 1
            return True
        return False

    """ 
      JOBS
    """
    def low_job(self):
        if self.sex == 'm':
            if random() < (0.2 + self.ambition_bonus - self.unambitious_bonus):
                self.state = 'medium job'
                self.promote()
                return True
        else: 
            if self.mobile:
                if random() < (0.05 + self.ambition_bonus - self.unambitious_bonus):
                    self.state = 'medium job'
                    self.promote()
                    return True
            if self.married:
                if random() < (0.3 - self.ambition_bonus + -1 * self.unambitious_bonus): 
                    self.state == 'stay at home'
                    return True
        return False

    def medium_job(self):
        if self.sex == 'm':
            if random() < (0.15 + self.ambition_bonus - self.unambitious_bonus): 
                self.state = 'high job'
                self.promote()
                return True
        else:
            if self.mobile: 
                if random() < (0.1 + self.ambition_bonus - self.unambitious_bonus): 
                    self.state = 'high job'
                    self.promote()
                    return True
            if self.married:
                if random() < (0.5 - self.ambition_bonus + -1 * self.unambitious_bonus): 
                    self.state == 'stay at home'
                    return True
        return False

    def high_job(self):
        if self.sex == 'm':
            if random() < (0.07 + self.ambition_bonus - self.unambitious_bonus): 
                self.state = 'very high job'
                self.promote()
                return True
        else:
            if self.mobile:
                if random() < (0.015 + self.ambition_bonus - self.unambitious_bonus): 
                    self.state = 'very high job'
                    self.promote()
                    return True
            
        return False

    def very_high_job(self):
        return False

    """ 
      HELP FUNCTION
    """
    def get_colleague(self): 
        sex = 'm' if random() < 0.8 else 'f'
        age = self.age + 10
        return Person(self.location[2], sex, age=age)

    def trauma_modifier(self):
        mod = 0
        trauma_expressions = [
            'gambler', 'drug addict', 'grifter', 'depressed',
            'anxiety disorder', 'grifter', 'paranoid', 'conspiracy theorist', 
            'suicidal', 'possesive'
            ]
        for d in trauma_expressions:
            if self.tags[d]:
                mod += 1
        return mod / 8

    def promote(self):
        self.income += 1
        if self.live_above_pay():
            if self.lifestyle < 2: 
                self.lifestyle += 2
            elif self.lifestyle < 3: 
                self.lifestyle += 1
        else: 
            if self.lifestyle < 3: 
                self.lifestyle += 1

        if self.sex == 'm':
            self.job = male_jobs[self.career][0][self.income]

    def live_above_pay(self):
        return True if self.aspirations['lifestyle'] > self.income else False

    def log_change(self):
        log = {
            'age' : self.age,
            'state' : self.state, 
            'income' : income[self.income], 
            'location' : self.location, 
            'lifestyle' : lifestyle[self.lifestyle], 
            'job' : self.job,
        }
        if self.sex == 'm': 
            log['career'] = self.career
        
        log['married'] = self.married 

        if self.state not in ['student', 'unemployed', 'jailed', 'stay at home']:
            log['boss'] = self.people['boss'].__str__()
            log['colleague'] = self.people['colleague'].__str__()

        if self.state == 'jailed':
            log['crime'] = self.crime
            log['serving time'] = self.punishment
        
        self.log[self.year] = log

    def get_log(self):
        return self.log

    """ 
      TRIGGERS
    """
    def send_to_jail(self, crime='stealing', serving_time=9): 
        self.crime = crime
        self.serving_time = serving_time
        self.punishment = serving_time
        self.state = 'jailed'

    def fire(self):
        self.state = 'unemployed'
        self.income = 0
        self.lifestyle = 1 if self.live_above_pay() else 0


class IOLife:
    def __init__(self, people, location, guardian, tags, sex, age1945) -> None:
        self.people = people     
        self.sex = sex
        self.location = location
        self.guardian = guardian
        self.year = 1945
        self.tags = tags
        self.age = age1945

    def init_people(self):
        g = Person('Australia', self.guardian['sex'], self.guardian['name'], self.guardian['surname'])
        g.age = self.guardian['age'] + (self.year - 1945)
        self.people['guardian'] = g
        self.people['bestfriend'] = self.make_person()
        self.people['childhoodfriend'] = self.make_person()
        self.people['childhoodfriend'].age = self.age
        self.people['friend'] = self.make_person()

    def transition(self, people, location, tags):
        if self.age == 18:
            self.init_people()
        if self.age > 17:
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

        if random() < 0.3: 
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

    """ 
      TRIGGERS
    """
    def trigger(self, trigger, romance, professional):
        return romance, professional

