input_alphabet = set(" \t\n")

states = {'s1', 's2'}

rules = {
    's1': {' ': 's2',
           '\t': 's2',
           '\n': 's2',
           },
    's2': {' ': 's2',
           '\t': 's2',
           '\n': 's2',
           },
}

initial_state = 's1'
terminate_state = {'s2'}
