from pda.pda import PDA
from pda.string_perserver import perserve_string
from lexer.data import ws_data

import unittest


class TestWhiteSpacePDA(unittest.TestCase):
    def test_pda_positive(self):
        pda_ws = PDA(ws_data.rules,
                     ws_data.input_alphabet,
                     ws_data.states,
                     ws_data.initial_state,
                     ws_data.terminate_state)
        self.assertEqual(pda_ws.state, 's1')

        pda_ws.input(' ')
        self.assertEqual(pda_ws.state, 's2')
        self.assertTrue(pda_ws.in_terminate_state())

    def test_pda_perserve(self):
        pda_ws = PDA(ws_data.rules,
                     ws_data.input_alphabet,
                     ws_data.states,
                     ws_data.initial_state,
                     ws_data.terminate_state)
        self.assertEqual((True, 0), perserve_string(' rk', pda_ws, 0))

if __name__ == '__main__':
    unittest.main()
