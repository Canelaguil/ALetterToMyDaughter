
traits = [
    ('curious', 'disinterested'),
    ('organised', 'disorganised'),
    ('moody', 'calm'),
    ('critical', 'tolerant'), 
    ('quirky', 'straight-laced'),
    ('egocentric', 'humble'), 
    ('creative', 'dull'),
    ('moral', 'immoral'),
    ('impulsive', 'thoughtful'),
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
    ('cheeky', 'humorless')
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
    'A' : {
        'name' : 'A', 
        'surname' : 'Aa', 
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
        'allowance' : allowance[1]
    },
    'B' : {
        'name' : 'B', 
        'surname' : 'Bb', 
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
        'allowance' : allowance[-1]
    },
    'C' : {
        'name' : 'C', 
        'surname' : 'Cc', 
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
        'allowance' : allowance[0]
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
        'allowance' : allowance[0]
    }
}
