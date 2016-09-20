import pda
import string_perserver as s_p

input_alphabet = {'a', 'b', 'c'}

states = {'s1', 's2', 's3'}

rules = {
	's1': {'a': 's1', 'b': 's2', 'c': 's3'},
	's2': {'a': 's2', 'b': 's2', 'c': 's3'},
	's3': {'a': 's2', 'b': 's1', 'c': 's3'}
}

initial_state = 's1'
terminate_state = 's3'

my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)

'''print my_pda.state

my_pda.input('a')

print my_pda.state

my_pda.input('c')

print my_pda.state
print my_pda.in_terminate_state()'''

print s_p.perserve_string('aaabbacabc', my_pda, 0)