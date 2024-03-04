import re

regex_L = r".*khirby.calma.*"

import graphviz

# Define DFA states
states = ['q0', 'q1', 'q2', 'q3', 'q4']

# Define alphabet (summation) 
# FIXME: the alphabet is not complete
alphabet = ['a', 'b', 'c', 'd', 'e', 'f']


# Define transition
# FIXME: the transition is not complete
transition = {
	'q0': {'a': 'q0', 'b': 'q0'},
	'q1': {'h': 'q2'},
	'q2': {'i': 'q3'},
	'q3': {'r': 'q4'},
	'q4': {'b': 'q4', 'a': 'q4'}
}

# Define initial and accepting states


# Create and visualize the DFA
