
traits = [
    ('curious', 'disinterested'),
    ('organised', 'disorganised'),
    ('moody', 'calm'),
    ('critical', 'tolerant'), 
    ('quirky', 'straight-laced'),
    ('egocentric', 'humble'), 
    ('creative', 'dull'),
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

allowance = [
    'no allowance', 'small allowance', 
    'medium allowance', 'big allowance'
    ]
guardians = {
    1 : {
        'name' : 'Kent', 
        'surname' : 'Roberts', 
        'age' : 32,
        'relation' : 'cousin',
        'location' : 'Aaa',
        'income_class' : 'medium',
        'lifestyle' : 'average', 
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
        'name' : 'James', 
        'surname' : 'Lee', 
        'age' : 72,
        'relation' : 'uncle',
        'location' : 'Bbb',
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
        'name' : 'Magda', 
        'surname' : 'Martin', 
        'age' : 55,
        'relation' : 'sister',
        'location' : 'Ccc',
        'income_class' : 'high',
        'lifestyle' : 'lavish', 
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
        'location' : 'Ddd',
        'income_class' : 'low',
        'lifestyle' : 'humble', 
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
