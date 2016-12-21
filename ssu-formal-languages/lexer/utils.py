import sys
sys.path.insert(0, '/home/imperat/SSU-Courses/ssu-formal-languages')

from pda.pda import PDA
from termcolor import colored


def generate_pda_for_word(word, meta=None, prior=None):
    input_alphabet = set(word)
    states = range(255)[:len(word)+1]
    rules = {i: {word[i]: i+1} for i, _ in enumerate(word)}
    initial_state = states[0]
    terminate_state = {states[-1]}
    pda = PDA(rules, input_alphabet, states, initial_state, terminate_state)
    pda.meta = meta
    if prior:
        pda.prior = prior
    return pda


class Token(object):
    """ Token is object that needed for processing
    syntax analys of language """

    def __init__(self, token_type, content=None):
        self.token_type = token_type
        self.content = content

    def print_token(self):
        token_type = self.token_type + " " * (13 - len(self.token_type))
        if self.token_type == 'whitespace':
            self.content = " "
        colors = {"keyword": "red", "bool": "blue"}
        color = colors.get(self.token_type, "white")
        if self.content:
            print colored("%s <%s>" % (token_type, self.content),
                          color)

    def __eq__(self, other):
        if other is not None:
            return self.token_type == other.token_type
        return False

    def __str__(self):
        return "%s" % (self.token_type)

    def __repr__(self):
        return self.__str__()

    def postfix(self, s):
        self.token_type += s
