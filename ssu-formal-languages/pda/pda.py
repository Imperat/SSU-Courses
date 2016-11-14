import pda_exceptions as e

class PDA(object):
    def __init__(self, rules, input_alphabet, states,
                 initial_state, terminate_states):

        self.rules = rules
        self.input_alphabet = input_alphabet
        self.states = states
        self.state = initial_state
        self.terminate_states = terminate_states
        self.crash = False

    def _crash(self):
        self.crash = True

    def input(self, symbol):
        # print symbol + "- - " + self.state
        try:
            if self.crash:
                raise e.PDACrashException(
                    "Error by input. PDA is crashed!")
            self.state = self.rules[self.state][symbol]
        except KeyError:
            if symbol not in self.input_alphabet:
                self._crash()
                raise e.UnknownSymbolException(
                    "Symbol isn't in input alphabet")
            else:
                self._crash()
                raise e.PDACrashException(
                    "PDA is crashed")

    def in_terminate_state(self):
        return self.state in self.terminate_states
