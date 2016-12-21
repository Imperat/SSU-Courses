# coding: utf-8

import sys
sys.path.insert(0, '/home/imperat/SSU-Courses/ssu-formal-languages')

from lexer.lexer import main as get_tokens
from lexer.utils import Token

import copy
import logging
#tokens = get_tokens()
#for token in tokens:
#    token.print_token()


class ContextFreeGrammarRule(object):

    def __init__(self, left_token, right_tokens):
        self.left_token = left_token
        self.right_tokens = right_tokens

    def __eq__(self, other):
        return (self.left_token == other.left_token and
                self.right_tokens == other.right_tokens)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "%s --> %s" % (self.left_token, self.right_tokens)


class ContextFreeGrammarRuleChain(object):

    def __init__(self, rule, dot_position):
        self.rule = rule
        self.dot_position = dot_position

    def get_directed_symbol(self):
        if len(self.rule.right_tokens) > self.dot_position:
            return self.rule.right_tokens[self.dot_position]
        return None

    def get_follow_symbol(self):
        try:
            return self.rule.right_tokens[self.dot_position + 1]
        except IndexError:
            return None

    def __eq__(self, other):
        if self.__repr__() == str(other):
            if self.rule != other.rule:
                import pdb; pdb.set_trace()
        return ((self.rule == other.rule) and
                (self.dot_position == other.dot_position))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self.rule) + (" [%s]" % self.dot_position)


class ContextFreeGrammar(object):

    def __init__(self, terms, non_terms, start_symbol, rules):
        self.terms = terms
        self.non_terms = non_terms
        self.start_symbol = start_symbol
        self.rules = rules


    def get_grammar_symbols(self):
        return self.terms + self.non_terms


class SyntaxAnalyzer(object):

    def __init__(self, grammar):
        self.grammar = grammar
        self.__extend_grammar()

    def __extend_grammar(self):
        old_start_symbol = self.grammar.start_symbol
        new_start_symbol = copy.deepcopy(self.grammar.start_symbol)
        new_start_symbol.postfix('/')
        self.grammar.start_symbol = new_start_symbol
        self.grammar.non_terms.insert(0, new_start_symbol)
        self.grammar.rules.insert(
        0, ContextFreeGrammarRule(new_start_symbol, [old_start_symbol])
        )


    def closure(self, I):
        J = copy.deepcopy(I)
        while True:
            k = 0
            for A in J:
                for B in self.grammar.rules:
                    if B.left_token == A.get_directed_symbol():
                        chain = ContextFreeGrammarRuleChain(B, 0)
                        if chain not in J:
                            J.append(chain)
                            k += 1
            if k == 0:
                break
        return J

    def goto(self, I, X):
        J = []
        for A in I:
            if X == A.get_directed_symbol():
                chain = ContextFreeGrammarRuleChain(A.rule,
                                                    A.dot_position + 1)
                J.append(chain)
        return self.closure(J)

    def cannonical_set(self):
        start_chain = ContextFreeGrammarRuleChain(
                        self.grammar.rules[0], 0)
        C = [self.closure([start_chain])]
        for I in C:
            for X in self.grammar.get_grammar_symbols():
                if self.goto(I, X) and self.goto(I, X) not in C:
                    C.append(self.goto(I, X))
        return C

    def analis(self):
        C = self.cannonical_set()
        stack = [0]
        tokens = list(filter(lambda x: x.token_type != 'whitespace',
                             get_tokens()))
        tokens = [Token('id'), Token('*'), Token('id'), Token('+'), Token('id')]
        state = C[0]
        stri = 1
        print "String     Stack      Input"
        while True:
            print "%s          %s     %s" % (stri, stack, tokens)
            stri += 1
            try:
                token = tokens.pop(0)
                old_state = copy.deepcopy(state)
                state = self.goto(state, token)
                no_tokens = False
            except:
                state = []
                no_tokens = True

            try:
                position = C.index(state)
                stack.append(position)
            except:
                if not no_tokens:
                    tokens.insert(0, token)
                chain = C[stack[-1]][0]
                left_token, right_tokens = chain.rule.left_token, chain.rule.right_tokens
                devnull = []
                for i in range(len(right_tokens)):
                    devnull.append(stack.pop())
                tokens.insert(0, left_token)
                if self.grammar.start_symbol == left_token:
                    print "SUCESS"
                    exit()
                state = C[stack[-1]]
