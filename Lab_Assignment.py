import re

regex_L = r".*khirby.calma.*"

import graphviz

# Define alphabet (sigma) 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Define transitions
def createTransition(sigmaTransition, customTransitions = {}): 
	transitions = {}
	for letter in alphabet:
		if letter in customTransitions:
			transitions[letter] = customTransitions[letter]
		else:
			transitions[letter] = sigmaTransition
	return transitions

qStatesAndTransitions = {
	'q0': createTransition('q0', {'k': 'q1'}),
	'q1': createTransition('q0', {'h': 'q2', 'k': 'q1'}),
	'q2': createTransition('q0', {'i': 'q3'}),
	'q3': createTransition('q0', {'r': 'q4'}),
	'q4': createTransition('q0', {'b': 'q5'}),
	'q5': createTransition('q0', {'y': 'q6'}),
	'q6': createTransition('q6', {'c': 'q7'}),
	'q7': createTransition('q6', {'a': 'q8', 'c': 'q7'}),
	'q8': createTransition('q6', {'l': 'q9'}),
	'q9': createTransition('q6', {'m': 'q10'}),
	'q10': createTransition('q6', {'a': 'q11'}),
	'q11': createTransition('q11'),
}

# Create and visualize the DFA
def DFA(transitions, string):
	startState = 'q0'
	currentState = startState
	acceptingState = 'q11'
	for letter in string:
		currentState = transitions[currentState][letter]
	if (currentState == acceptingState):
		return 'Accept'
	else:
		return 'Reject'

# no randomsubstring 
testString = 'khirbycalma'
dfaOutput = DFA(qStatesAndTransitions, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# random substring front
testString = 'dsfsuyfbqbidskkhirbycalma'
dfaOutput = DFA(qStatesAndTransitions, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')


# random substring middle
testString = 'khirbydfigufdguibdfvccalma'
dfaOutput = DFA(qStatesAndTransitions, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# random substring end
testString = 'khirbycalmaaciuerafbdskjfb'
dfaOutput = DFA(qStatesAndTransitions, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# random substring everywhere
testString = 'sdifhsuifsakkhirbysdofsofsoojccalmaaciuerafbdskjfb'
dfaOutput = DFA(qStatesAndTransitions, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# empty string
testString = ''
dfaOutput = DFA(qStatesAndTransitions, testString)
expectedOutput = 'Reject'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# misspelled first name
testString = 'kirbycalma'
dfaOutput = DFA(qStatesAndTransitions, testString)
expectedOutput = 'Reject'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# misspelled last name
testString = 'khirbycalm'
dfaOutput = DFA(qStatesAndTransitions, testString)
expectedOutput = 'Reject'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')
