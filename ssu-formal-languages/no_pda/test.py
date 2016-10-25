import no_pda
import string_perserver as s_p

import unittest


class TestHelper(object):
    @staticmethod
    def get_test_no_pda():
        input_alphabet = {'a', 'b', 'c'}

        states = {'s1', 's2', 's3'}
        
        rules = {
            's1': {'a': 's1', 'b': 's2', 'c': 's3'},
            's2': {'a': 's2', 'b': 's2', 'c': 's3'},
            's3': {'a': 's2', 'b': 's1', 'c': 's3'}
        }
        
        initial_state = {'s1', 's2'}
        terminate_states = {'s3'}
        
        my_no_pda = no_pda.NOPDA(rules, input_alphabet, states,
                                 initial_state, terminate_state)

        return my_no_pda


class TestPDA(unittest.TestCase):
    def test_NOPDA(self):
        my_pda = TestHelper.get_test_no_pda()
        self.assertEqual(my_pda.state, 's1')

        my_pda.input('a')
        self.assertEqual(my_pda.state, 's1')

        my_pda.input('c')
        self.assertEqual(my_pda.state, 's3')

        my_pda.input('a')
        self.assertEqual(my_pda.state, 's2')

        my_pda.input('c')
        self.assertEqual(my_pda.state, 's3')
        self.assertTrue(my_pda.in_terminate_state())


class TestStringPerserver(unittest.TestCase):
    def test_string_perserver(self):
        my_pda = TestHelper.get_test_no_pda()
        res = s_p.perserve_string('aaabbacabc', my_no_pda, 0)
        self.assertEqual(res, (True, 9))

        my_pda = TestHelper.get_test_no_pda()
        res = s_p.perserve_string('aaabbacabc', my_no_pda, 3)
        self.assertEqual(res, (True, 9))

if __name__ == '__main__':
    unittest.main()