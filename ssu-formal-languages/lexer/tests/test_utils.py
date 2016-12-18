import sys
sys.path.insert(0, '/home/imperat/SSU-Courses/ssu-formal-languages')

from lexer import utils

import unittest


class TestUtils(unittest.TestCase):
    def test_generate_pda_for_word(self):
        PDA = utils.generate_pda_for_word('delete')
        self.assertEqual(PDA.state, 0)
        for i, s in enumerate('delete'):
            PDA.input(s)
            self.assertEqual(PDA.state, i+1)
        self.assertTrue(PDA.in_terminate_state())

if __name__ == '__main__':
    unittest.main()
