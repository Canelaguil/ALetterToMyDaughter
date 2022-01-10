
traits = [
    ('curious', 'disinterested'),
    ('organised', 'disorganised'),
    ('moody', 'calm'),
    ('critical', 'tolerant'), 
    ('quirky', 'straight-laced'),
    ('egocentric', 'humble'), 
    ('creative', 'dull'),
    ('ambitious', 'unambitious'),
    ('moral', 'immoral'),
    ('relaxed', 'uptight'),
    ('impulsive', 'hesitant'),
    ('optimistic', 'pessimistic'),
    ('obedient', 'rebellious'),
    ('brave', 'cowardly'),
    ('nervous', 'confident'),
    ('workaholic', 'lazy'),
    ('outgoing', 'shy'),
    ('clumsy', 'athletic'),
    ('intelligent', 'slow'),
    ('kind', 'mean'),
    ('timid', 'exuberant'),
    ('melancholic', 'upbeat'),
    ('daydreamer', 'practical'),
    ('suspicious', 'naive'), 
    ('cheeky', 'humorless'), 
    ('empathetic', 'cold'), 
    ('altruistic', 'selfish'),
    ('stoic', 'sensitive'), 
    ('jealous', 'trusting')
    ]

adult_tags = {
    # relationships
    'divorced' : False, 
    'married' : False,
    'relationship' : False,
    'parent' : False, 
    'widowed' : False,
    'commitment-averse' : False,
    # jobs
    'famous' : False, 
    'unambitious' : False,
    'independent' : False,
    'creative' : False, 
    # trauma
    'gambler' : False, 
    'drug addict' : False, 
    'grifter' : False, 
    'anxiety disorder' : False, 
    'depressed' : False, 
    'paranoid' : False,
    'recovering' : False,
    'conpiracy theorist' : False,
    'suicidal' : False,
    'possesive' : False,
    # random
    'wheelchair-bound' : False, 
    'blind' : False, 
    'hippy' : False, 
    'spiritualist' : False, 
    'evangelist' : False,
    'strict' : False, 
}

people = {
    # Romantic  / family life
    'love_interest' : None, 
    'old_flame' : None, 
    'partner' : None, 
    'spouse' : None, 
    'affairpartner' : None, 
    'dead_partner' : None,
    'dead_child' : None,
    'children' : [], 
    'extra_marital_children' : [],
    'ex_spouses' : [],
    'ex_partners' : [], 
    # Professional life
    'boss'  : None, 
    'colleague' : None, 
    # IO Life
    'guardian' : None, 
    'friend' : None, 
    'bestfriend' : None, 
    'deadfriend' : None, 
    'bfriend' : None, 
    'childhoodfriend' : None,
    'familyfriend' : None, 
    'pet' : None, 
    'enemy' : None, 
}

"""
GUARDIANS
"""
allowance = [
    'no allowance', 'small allowance', 
    'medium allowance', 'big allowance']

guardians = {
    1 : {
        'name' : 'April', 
        'surname' : 'Ryan', 
        'age' : 32,
        'sex' : 'f',
        'relation' : 'cousin',
        'location' : ('Port Macquarie', 'New South Wales', 'Australia', 'town'),
        'income_class' : 1,
        'lifestyle' : 1, 
        'married' : True,
        'other_children' : True,
        'nurturing' : True, 
        'provide_college' : False,
        'provide_women_college' : False,
        'provide_boarding_school' : False, 
        'allowance' : allowance[1], 
        'capacity' : 1,
        'ward' : []
    },
    2 : {
        'name' : 'Paul', 
        'surname' : 'Carter', 
        'age' : 72,
        'sex' : 'm',
        'relation' : 'uncle',
        'location' : ('Yankalilla', 'South Australia', 'Australia', 'town'),
        'income_class' : 3,
        'lifestyle' : 3, 
        'married' : False,
        'other_children' : False,
        'nurturing' : True, 
        'provide_college' : True,
        'provide_women_college' : False,
        'provide_boarding_school' : False, 
        'allowance' : allowance[-1],
        'capacity' : 1,
        'ward' : []
    },
    3 : {
        'name' : 'Diane', 
        'surname' : 'Schwarze', 
        'age' : 55,
        'sex' : 'f',
        'relation' : 'sister',
        'location' : ('Geelong', 'Victoria', 'Australia', 'town'),
        'income_class' : 2,
        'lifestyle' : 3, 
        'married' : True,
        'other_children' : False,
        'nurturing' : False, 
        'provide_college' : True,
        'provide_women_college' : True,
        'provide_boarding_school' : True, 
        'allowance' : allowance[2],
        'capacity' : 2,
        'ward' : []
    },
    'nadia' : {
        'name' : 'Nadia', 
        'surname' : 'Wilkes', 
        'age' : 47,
        'sex' : 'f',
        'age1940' : 42, 
        'relation' : 'governess',
        'location' : ('Yealering', 'Western Australia', 'Australia', 'town'),
        'income_class' : 0,
        'lifestyle' : 0, 
        'married' : False,
        'other_children' : False,
        'nurturing' : True, 
        'provide_college' : False,
        'provide_women_college' : False,
        'provide_boarding_school' : False, 
        'allowance' : allowance[0],
        'capacity' : 1,
        'ward' : []
    }
}

"""
NAMES
"""

fem_first_en = ['Linda', 'Mary', 'Patricia', 'Susan', 'Barbara', 'Nancy', 'Deborah', 'Dawn', 'Cathleen', 'Catherine', 'Danielle', 'Karin', 'Ingrid', 'Helga', 'Renate', 'Elke', 'Ursula', 'Erika', 'Christa', 'Gisela', 'Monika', 'Hannelore', 'Inge', 'Christel', 'Rosemarie', 'Ingeborg', 'Brigitte', 'Bärbel', 'Waltraud', 'Jutta', 'Ute', 'Mary', 'Linda', 'Barbara', 'Patricia', 'Carol', 'Sandra', 'Nancy', 'Sharon', 'Judith', 'Susan', 'Betty', 'Carolyn', 'Margaret', 'Shirley', 'Judy', 'Karen', 'Donna', 'Kathleen', 'Joyce', 'Dorothy', 'Janet', 'Diane', 'Janice', 'Joan', 'Elizabeth', 'Brenda', 'Gloria', 'Virginia', 'Marilyn', 'Martha', 'Beverly', 'Helen', 'Bonnie', 'Ruth', 'Frances', 'Jean', 'Ann', 'Phyllis', 'Pamela', 'Jane', 'Alice', 'Peggy', 'Cheryl', 'Doris', 'Catherine', 'Elaine', 'Cynthia', 'Marie', 'Lois', 'Connie']
male_first_en = ['Robert', 'Michael', 'John', 'David', 'Richard', 'Thomas', 'Mark', 'James', 'William', 'Charles', 'Steven', 'George', 'Peter', 'Klaus', 'Hans', 'Jürgen', 'Dieter', 'Günter', 'Horst', 'Manfred', 'Uwe', 'Wolfgang', 'Carl', 'Werner', 'Rolf', 'Heinz', 'Gerhard', 'Helmut', 'Gerd', 'Bernd', 'Walter', 'Harald', 'James', 'Robert', 'John', 'William', 'Richard', 'David', 'Charles', 'Thomas', 'Michael', 'Ronald', 'Larry', 'Donald', 'Joseph', 'Gary', 'George', 'Kenneth', 'Paul', 'Edward', 'Jerry', 'Dennis', 'Frank', 'Daniel', 'Raymond', 'Roger', 'Stephen', 'Gerald', 'Walter', 'Harold', 'Steven', 'Douglas', 'Lawrence', 'Terry', 'Wayne', 'Arthur', 'Jack', 'Carl', 'Henry', 'Willie', 'Bruce', 'Joe', 'Peter', 'Billy', 'Roy', 'Ralph', 'Anthony', 'Jimmy', 'Albert', 'Bobby', 'Eugene', 'Johnny']
fem_first_nl = ['Maaike', 'Rosa', 'Myrthe', 'Tamara', 'Nicole', 'Riet', 'Henrietta', 'Annie', 'Marie Jose', 'Leanne', 'Maria', 'Rieky', 'Suze', 'Hasse', 'Annemarie', 'Mare', 'Roos', 'Lisa', 'Celine', 'Anna', 'Sofia', 'Sonja', 'Floor', 'Fleur', 'Nicole', 'Martha', 'Brechtje', 'Kathleen', 'Louise', 'Aagje', 'Evelien', 'Lotte', 'Loes', 'Guusje', 'Ada', 'Katootje', 'Willemijn', 'Sien', 'Madelief', 'Jet', 'Tjitske']
male_first_nl = ['Tijs', 'Joris', 'Jonathan', 'Niels', 'Jurre', 'Wouter', 'Julian', 'Lars', 'Daniel', 'Mathias', 'Mathijs', 'Daan', 'Dirk', 'Hugo', 'Aart', 'Koen', 'Jan', 'Huub', 'Kees', 'Gosse', 'Guus', 'Hein', 'Willem', 'Teun', 'Rein', 'Leendert', 'Krijn', 'Siem', 'Adriaan', 'Joost', 'Hendrik', 'Gerrit', 'Lennart', 'Paul', 'Waldemar', 'Bertus', 'Beppe', 'Arjan', 'Koos', 'Wim', 'Sietse', 'Piet', 'Dik', 'Sjors']
surnames_en = ['Acker', 'Ackford', 'Ansley', 'Barlow', 'Bircher', 'Catfield', 'Calcott', 'Digby', 'Eveleigh', 'Farlow', 'Fulton', 'Gladstone', 'Hanney', 'Harlow', 'Hayes', 'Hilling', 'Kilby', 'Marleigh', 'Marston', 'Morley', 'Quinton', 'Ramsay', 'Riley', 'Shelly', 'Sherwood', 'Tindall', 'Thorpe', 'Woolley', 'York', 'Yeaton', 'Ditterich', 'Bolte', 'Brennan', 'Fischer', 'Frei', 'Fittler', 'Monash', 'von Mueller', 'Neumann', 'Seibold', 'Springborg', 'Zusak']
surnames_nl = ['Teulings', 'van Hijfte', 'Smeets', 'Potharst', 'Bosch', 'De Wolf', 'Timmerman', 'Verweij', 'van Veenen', 'ter Schure', 'Verhoeven', 'De Jong', 'Misdorp', 'de Valk', 'Perdeck', 'Brandsen', 'Jonk', 'Wassing', 'Slagt', 'van Kooten', 'de Bie', 'Schippers', 'van Nieuwkerken', 'Klinkhamer', 'van Zuilichem', 'von Zesen', 'Kolodziej']


"""
LOCATIONS
"""

locations = [
    ('Yealering', 'Western Australia', 'Australia', 'town'),
    ('Geelong', 'Victoria', 'Australia', 'town'),
    ('Yankalilla', 'South Australia', 'Australia', 'town'),
    ('Port Macquarie', 'New South Wales', 'Australia', 'town'),
    ('Sydney', 'New South Wales', 'Australia', 'city'),
    ('Adelaide', 'South Australia', 'Australia', 'city'),
    ('Melbourne', 'Victoria', 'Australia', 'city'),
    ('Perth', 'Western Australia', 'Australia', 'city'),
    ('Amsterdam', 'Noord-Holland', 'Netherlands', 'city'),
    ('Amersfoort', 'Utrecht', 'Netherlands', 'town')
]


""" 
  JOBS
"""

lifestyle = ['humble', 'middle class', 'rich', 'lavish' ]
income = ['low', 'medium', 'high', 'very high']

# (title, level, acceptable, mobile, respectable, student)
fem_jobs = [
    ('writer', 'creative', True, True, True, False),
    ('painter', 'creative', True, True, True, False),
    ('actress', 'creative', False, True, True, False), 
    ('singer', 'creative', False, True, True, False), 
    ('shop keep', 'low', False, False, True, False), 
    ('sex worker', 'low', False, False, False, False), 
    ('bar keep', 'low', False, False, True, False),
    ('teacher', 'medium', True, False, True, False), 
    ('nurse', 'medium', True, False, True, False), 
    ('journalist', 'medium', False, True, True, False), 
    ('librarian', 'medium', False, False, True, False), 
    ('pharmacist', 'medium', False, True, True, True), 
    ('secretary', 'medium', False, False, True, False),
    ('real estate agent', 'medium', False, False, True, False),
    ('store owner', 'high', False, True, True, False),
    ('doctor', 'high', False, False, True, True)
]

# title : (0 job per income class, 1 student, 2 acceptable, 3 respectable)
male_jobs = {
    'accountant' : (['clerk', 'accountant', 'senior accountant', 'CFO'], False, True, True),
    'laywer' : ([None, 'paralegal apprenticeship', 'paralegal', 'sollicitor'], True, True, True),
    'bar' : (['bartender', 'bar owner', 'bar chain owner', 'CEO bar chain'], False, False, True), 
    'mechanic' : (['mechanic apprentice', 'mechanic', 'car shop owner', None], False, False, True), 
    'cook' : (['waiter', 'line cook', 'chef cook', 'famous chef cook'], False, False, True),
    'sex worker' : (['sex worker', 'escort', 'brothel owner', None], False, False, False)
}
