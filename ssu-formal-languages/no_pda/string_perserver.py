import no_pda_exceptions as e
import no_pda as p

def perserve_string(string, no_pda, n):
    current_string = string[n:]
    word_is_admit = False
    terminate_position = None
    for i,s in enumerate(current_string):
        try:
            no_pda.input(s)
            if no_pda.in_terminate_state():
                word_is_admit = True
                terminate_position = n + i
        except e.UnknownSymbolException:
            return word_is_admit, terminate_position
    return word_is_admit, terminate_position

