import sys
sys.path.insert(0, '/home/imperat/SSU-Courses/ssu-formal-languages')

from pda.string_perserver import perserve_string
from pda.pda import PDA

from lexer.data import float_data
from lexer.data import int_data
from lexer.data import ws_data
from lexer.data import id_data
from lexer.utils import generate_pda_for_word
from lexer.utils import Token


def generate_start_authos():
    pda_float = PDA(float_data.rules,
                    float_data.input_alphabet,
                    float_data.states,
                    float_data.initial_state,
                    float_data.terminate_state)

    pda_float.prior = 0
    pda_float.meta = 'float'

    pda_int = PDA(int_data.rules,
                  int_data.input_alphabet,
                  int_data.states,
                  int_data.initial_state,
                  int_data.terminate_state)

    pda_int.prior = 1
    pda_int.meta = 'int'

    lst_pda_KW = []
    for word in ['var', 'fun', 'in', 'let', 'end', 'if', 'then', 'else', 'val']:
        lst_pda_KW.append(generate_pda_for_word(word, 'keyword', prior=5))

    lst_pda_LOG = []
    for word in ['true', 'false']:
        lst_pda_LOG.append(generate_pda_for_word(word, 'bool', prior=6))

    lst_pda_OP = []
    for word in ['+', '-' ,'*' ,'/' , 'andalso', 'orelse', 'not']:
        lst_pda_OP.append(generate_pda_for_word(word, 'operator', prior=7))

    lst_pda_AS = []
    for word in ['=']:
        lst_pda_AS.append(generate_pda_for_word(word, 'equal', prior=7))

    lst_pda_LB = []
    for word in ['(']:
        lst_pda_LB.append(generate_pda_for_word(word, 'left_bracket', prior=7))

    lst_pda_RB = []
    for word in [')']:
        lst_pda_RB.append(generate_pda_for_word(word, 'right_bracket', prior=7))

    pda_ws = PDA(ws_data.rules,
                 ws_data.input_alphabet,
                 ws_data.states,
                 ws_data.initial_state,
                 ws_data.terminate_state)

    pda_ws.meta = 'whitespace'
    pda_ws.prior = 10

    pda_id = PDA(id_data.rules,
                 id_data.input_alphabet,
                 id_data.states,
                 id_data.initial_state,
                 id_data.terminate_state)

    pda_id.meta = 'id'
    pda_id.prior = 3

    lst_pda_C = []
    for word in [',']:
        lst_pda_C.append(generate_pda_for_word(word, 'comma', prior=7))

    authos = []
    authos.extend([pda_float, pda_int, pda_ws, pda_id])
    authos.extend(lst_pda_KW)
    authos.extend(lst_pda_LOG)
    authos.extend(lst_pda_OP)
    authos.extend(lst_pda_AS)
    authos.extend(lst_pda_LB)
    authos.extend(lst_pda_RB)
    authos.extend(lst_pda_C)
    return authos

with open('programms/pr-1.programm') as f:
    program = f.read()
    current_position = 0
    metas = []
    while True:
        start_position = current_position
        leng, prior, meta = 0, 0, ''
        for auto in generate_start_authos():
            res = perserve_string(program, auto, start_position), auto.meta
            # print res, auto.meta
            if res[0][0]:
                #if auto.prior >= prior
                if res[0][1] + 1 > current_position:
                    prior = auto.prior
                    meta = Token(auto.meta,
                                 program[start_position:1 + res[0][1]])
                    current_position = res[0][1] + 1
                elif res[0][1] + 1 == current_position:
                    if auto.prior > prior:
                        prior = auto.prior
                        meta = Token(auto.meta,
                                     program[start_position:1 + res[0][1]])
        if start_position == current_position:
            break
        metas.append(meta)

    for meta in metas:
        meta.print_token()

    # Check word perservers!!!
    # start testing!!!yeeeees!
# print generate_start_authos()
