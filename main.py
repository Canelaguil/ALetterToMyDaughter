class MemoryEvent:
    def __init__(self, description, weight, pos_a=[], neg_a=[], neu_a=[], s_e={}):
        """
        A memory has: 
        - description "" : line of text describing event
        - weight [0-5] : how impactful is this information?
        - positively_affects [] : list of siblings positively implicated
        - negatively_affects [] : list of siblings negatively implicated
        - neutraly_affects [] : list of siblings involved, but not impacted by memory
        - status_effects { trait : modifier } : dictionary of traits and their modifiers
        """
        self.description = description
        self.weight = weight
        self.positively_affects = pos_a
        self.negatively_affects = neg_a
        self.neutraly_affects = neu_a
        self.status_effects = s_e 
        self.known_by = self.init_known()

    def init_known(self):
        """
        Simple init function for known_by.
        """
        known = []
        for l in [self.positively_affects, self.negatively_affects, self.neutraly_affects]:
            for p in l: 
                if p not in known:
                    known.append(p)
        return known

    def char_knows(self, char_key):
        """
        Add new character to list of people who knows about it.
        """
        if char_key not in self.known_by:
            self.known_by.append(char_key)

    def does_char_know(self, char_key):
        """
        Checks if character knows about memory.
        """
        return char_key in self.known_by

    def how_affects_char(self, char_key):
        """
        Checks how character is affected by memory.
        """ 
        if char_key in self.positively_affects:
            return "positive"
        if char_key in self.negatively_affects: 
            return "negative" 
        if char_key in self.neutraly_affects: 
            return "neutral" 
        return "not affected"

    
m = MemoryEvent('df', 3, ['1', '2'], ['3', '2'])
print(m.known_by)