import no_pda_exceptions as e

class NOPDA(object):
    def __init__(self, rules, input_alphabet, states,
                 initial_states, terminate_states):

        self.rules = rules
        self.input_alphabet = input_alphabet
        self.states = states
        self.current_state = initial_states
        self.terminate_states = terminate_states
        self.crash = False

    def _crash(self):
        self.crash = True

    def input(self, symbol):
        if self.crash:
            raise e.NOPDACrashException(
                "Error by input. PDA is crashed!")
        new_states = {}
        for state in self.states:
            try:
                '''
                TODO Need add checkers for UnknowSymbols Exception
                '''
                new_states.extend(self.rules[self.state][symbol])
            except Exception as e:
                pass
        if not new_states:
            self._crash()
        else:
            self.current_state = new_states

    def in_terminate_state(self):
        self.current_states & self.terminate_states


'''
input_alphabet = {'a', 'b', 'c'}

        states = {'s1', 's2', 's3'}
        
        rules = {'s1': {'a': ['s1'], 'b': ['s2'], 'c': ['s3']}, 's2': {'a': ['s2'], 'b': ['s2'], 'c': ['s3', 's1']}, 's3': {'a': ['s2'], 'b': ['s1'], 'c': ['s3']}}
'''