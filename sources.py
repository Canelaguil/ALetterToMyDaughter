
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

event_traits = [
    'wheelchair-bound', 
    'famous', 
    'blind', 
    'hippy', 
    'spiritualist', 
    'conpiracy theorist',
    'evangelist',
    'strict', 
    'suicidal',
    'possesive'
]

adult_tags = {
    'divorced' : False, 
    'married' : False,
    'relationship' : False,
    'parent' : False, 
    'widowed' : False,
    'gambler' : False, 
    'drug addict' : False, 
    'grifter' : False, 
    'anxiety disorder' : False, 
    'depressed' : False, 
    'happy' : False, 
    'paranoid' : False
}

"""
GUARDIANS & LIFESTYLE
"""

lifestyle = ['pauper', 'humble', 'average', 'rich', 'lavish' ]
income = ['very low', 'low', 'medium', 'high', 'very high']
allowance = [
    'no allowance', 'small allowance', 
    'medium allowance', 'big allowance'
    ]
guardians = {
    1 : {
        'name' : 'April', 
        'surname' : 'Ryan', 
        'age' : 32,
        'relation' : 'cousin',
        'location' : ('Port Macquarie', 'New South Wales', 'Australia', 'town'),
        'income_class' : income[2],
        'lifestyle' : lifestyle[2], 
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
        'relation' : 'uncle',
        'location' : ('Yankalilla', 'South Australia', 'Australia', 'town'),
        'income_class' : income[4],
        'lifestyle' : lifestyle[3], 
        'income_class' : 'high',
        'lifestyle' : 'lavish', 
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
        'relation' : 'sister',
        'location' : ('Geelong', 'Victoria', 'Australia', 'town'),
        'income_class' : income[2],
        'lifestyle' : lifestyle[3], 
        'married' : True,
        'other_children' : False,
        'nurturing' : False, 
        'provide_college' : True,
        'provide_women_college' : True,
        'provide_boarding_school' : True, 
        'allowance' : allowance[0],
        'capacity' : 2,
        'ward' : []
    },
    'nadia' : {
        'name' : 'Nadia', 
        'surname' : 'Wilkes', 
        'age' : 47,
        'age1940' : 42, 
        'relation' : 'governess',
        'location' : ('Yealering', 'Western Australia', 'Australia', 'town'),
        'income_class' : income[1],
        'lifestyle' : lifestyle[1], 
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
fem_first_nl = ['Maaike', 'Myrthe', 'Tamara', 'Nicole', 'Riet', 'Henrietta', 'Annie', 'Marie Jose', 'Leanne', 'Maria', 'Rieky', 'Suze', 'Hasse']
male_first_nl = ['Tijs', 'Joris', 'Jonathan', 'Niels', 'Jurre', 'Wouter', 'Julian', 'Lars', 'Daniel', 'Mathias', 'Mathijs', 'Daan', 'Dirk']
surnames_en = ['Acker', 'Ackford', 'Ansley', 'Barlow', 'Bircher', 'Catfield', 'Calcott', 'Digby', 'Eveleigh', 'Farlow', 'Fulton', 'Gladstone', 'Hanney', 'Harlow', 'Hayes', 'Hilling', 'Kilby', 'Marleigh', 'Marston', 'Morley', 'Quinton', 'Ramsay', 'Riley', 'Shelly', 'Sherwood', 'Tindall', 'Thorpe', 'Woolley', 'York', 'Yeaton']
surnames_nl = ['Teulings', 'van Hijfte', 'Smeets', 'Potharst', 'Bosch', 'De Wolf', 'Timmerman', 'Verweij', 'van Veenen', 'ter Schure', 'Verhoeven', 'De Jong', 'Misdorp', 'de Valk', 'Perdeck', 'Brandsen', 'Jonk', 'Wassing', 'Slagt', 'Simonsdochter']


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
