
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
        'location' : ('Port Macquarie', 'Australia'),
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
        'location' : ('Yankalilla', 'Australia'),
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
        'location' : ('Geelong', 'Australia'),
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
        'location' : ('Yealering', 'Australia'),
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

fem_first_en = ['Linda', 'Mary', 'Patricia', 'Susan', 'Barbara', 'Nancy', 'Deborah', 'Dawn', 'Cathleen', 'Catherine', 'Danielle']
male_first_en = ['Robert', 'Michael', 'John', 'David', 'Richard', 'Thomas', 'Mark', 'James', 'William', 'Charles', 'Steven', 'George']
fem_first_nl = ['Maaike', 'Myrthe', 'Tamara', 'Nicole', 'Riet', 'Henrietta', 'Annie', 'Marie Jose', 'Leanne', 'Maria', 'Rieky', 'Suze', 'Hasse']
male_first_nl = ['Tijs', 'Joris', 'Jonathan', 'Niels', 'Jurre', 'Wouter', 'Julian', 'Lars', 'Daniel', 'Mathias', 'Mathijs', 'Daan', 'Dirk']
surnames_en = ['Acker', 'Ackford', 'Ansley', 'Barlow', 'Bircher', 'Catfield', 'Calcott', 'Digby', 'Eveleigh', 'Farlow', 'Fulton', 'Gladstone', 'Hanney', 'Harlow', 'Hayes', 'Hilling', 'Kilby', 'Marleigh', 'Marston', 'Morley', 'Quinton', 'Ramsay', 'Riley', 'Shelly', 'Sherwood', 'Tindall', 'Thorpe', 'Woolley', 'York', 'Yeaton']
surnames_nl = ['Teulings', 'van Hijfte', 'Smeets', 'Potharst', 'Bosch', 'De Wolf', 'Timmerman', 'Verweij', 'van Veenen', 'ter Schure', 'Verhoeven', 'De Jong', 'Misdorp', 'de Valk', 'Perdeck', 'Brandsen', 'Jonk', 'Wassing', 'Slagt', 'Simonsdochter']
