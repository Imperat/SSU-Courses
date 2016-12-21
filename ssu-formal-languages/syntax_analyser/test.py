# coding: utf-8

import sys
sys.path.insert(0, '/home/imperat/SSU-Courses/ssu-formal-languages')

from main import *
from lexer.utils import Token

import unittest


class TestGrammarClasses(object):

    def test_common(self):
        E = Token('E')
        T = Token('T')
        F = Token('F')
        id = Token('id')
        mul = Token('*')
        add = Token('+')
        l_b = Token('(')
        r_b = Token(')')

        rules = [
            ContextFreeGrammarRule(E, [E, add, T]),
            ContextFreeGrammarRule(E, [T]),
            ContextFreeGrammarRule(T, [T, mul, F]),
            ContextFreeGrammarRule(T, [F]),
            ContextFreeGrammarRule(F, [l_b, E, r_b]),
            ContextFreeGrammarRule(F, [id])
        ]

        grammar = ContextFreeGrammar([E, T, F], [add, mul, r_b, l_b, id],
                                     E, rules)

        print "Old start symbol is %s" % grammar.start_symbol
        analyser = SyntaxAnalyzer(grammar)
        for rule in analyser.grammar.rules:
            print "%s --> %s" % (str(rule.left_token), str(rule.right_tokens))
        print "New start symbol is %s" % analyser.grammar.start_symbol

        # Tables research
        print "\n\n\n"
        closure = analyser.closure([ContextFreeGrammarRuleChain(
            analyser.grammar.rules[0], 0
        )])

        for chain in closure:
            print "%s --> %s (%s)" % (str(chain.rule.left_token),
                                     str(chain.rule.right_tokens),
                                     str(chain.dot_position))

        print "\n\n\n"
        chain1, chain2 = closure[:2]
        chain2.dot_position += 1
        print "GOTO"
        print [chain1, chain2]
        print "\n"
        goto = analyser.goto([chain1, chain2], add)
        for gt in goto:
            print gt

        print "\n\n\n"
        print "Cannonical set"
        for i,j in enumerate(analyser.cannonical_set()):
            print "%s" % i
            for a in j:
                print "  --- %s" % a

        #analis!
        print "\n\n\n"
        print "analis"
        analyser.analis()




test = TestGrammarClasses()
test.test_common()
