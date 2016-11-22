
def letter_transition(state):
    letters = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    return {i: state for i in letters}


def all_transition(state):
    letters = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_'
    return {i: state for i in letters}

input_alphabet = set(" \t\n")

states = {'s1', 's2'}

rules = {
    's1': letter_transition('s2'),
    's2': all_transition('s2')
}

initial_state = 's1'
terminate_state = {'s2'}
