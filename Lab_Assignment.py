# Define alphabet (sigma) 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

"""
Define transitions.

sigmaTransitionState: state where the current state goes to with sigma (referece DFA Diagram)
customTransitions: transitions where current state goes to different state that the sigma does not go to (referece DFA Diagram)
"""
def createTransition(sigmaTransitionState, customTransitions = {}): 
	transitions = {}
	for letter in alphabet:
		if letter in customTransitions:
			transitions[letter] = customTransitions[letter]
		else:
			transitions[letter] = sigmaTransitionState
	return transitions
# Uses above-function to create transitions for each state 
khirbyCalmaDFA = {
	'q0': createTransition('q0', {'k': 'q1'}),
	'q1': createTransition('q0', {'h': 'q2', 'k': 'q1'}),
	'q2': createTransition('q0', {'i': 'q3', 'k': 'q1'}),
	'q3': createTransition('q0', {'k': 'q1', 'r': 'q4'}),
	'q4': createTransition('q0', {'b': 'q5', 'k': 'q1'}),
	'q5': createTransition('q0', {'k': 'q1', 'y': 'q6'}),
	'q6': createTransition('q6', {'c': 'q7'}),
	'q7': createTransition('q6', {'a': 'q8', 'c': 'q7'}),
	'q8': createTransition('q6', {'c': 'q7', 'l': 'q9'}),
	'q9': createTransition('q6', {'c': 'q7', 'm': 'q10'}),
	'q10': createTransition('q6', {'c': 'q7', 'a': 'q11'}),
	'q11': createTransition('q11'),
}

# Create and visualize the DFA
def DFA(dfa, string):
	"""
	Define start and accept states.
	Set current state to start state at the beginning since that is where the beginning of the string begins.
	Define accept state that will be later comapred to the current state (accepts if matches).
	"""
	startState = 'q0'
	currentState = startState
	acceptingState = 'q11'
	"""
	Go though each letter in string.
	Update current state based on the current state's defined transition of the current letter.
	Also checks if current letter is valid via lowercase alphabet. If not valid, error.
	"""
	for letter in string:
		if letter not in alphabet:
			return 'Error: String has character that is not allowed in the alphabet.'
		else:
			currentState = dfa[currentState][letter]
	"""
	Finishes going through whole string.
	Check if current state (once the DFA went through the whole string) matches with the defined accepting state.
	"""
	if (currentState == acceptingState):
		return 'Accept'
	else:
		return 'Reject'

# no random substring 
testString = 'khirbycalma'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# random substring front
testString = 'dsfsuyfbqbidskkhirbycalma'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# random substring middle
testString = 'khirbydfigufdguibdfvccalma'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# random substring end
testString = 'khirbycalmaaciuerafbdskjfb'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# random substring everywhere
testString = 'sdifhsuifsakkhirbysdofsofsoojccalmaaciuerafbdskjfb'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# starting valid character (first name) in beginning substring 
testString = 'khikhirbycalma'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# starting valid character (last name) in middle substring 
testString = 'khirbycalcalma'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Accept'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# empty string
testString = ''
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Reject'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# misspelled first name
testString = 'kirbycalma'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Reject'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# misspelled last name
testString = 'khirbycalm'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Reject'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# invalid character beginning substring
testString = '&khirbycalma'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Error: String has character that is not allowed in the alphabet.'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# invalid character middle substring
testString = 'khirbyKcalma'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Error: String has character that is not allowed in the alphabet.'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')

# invalid character end substring
testString = 'khirbycalmaC'
dfaOutput = DFA(khirbyCalmaDFA, testString)
expectedOutput = 'Error: String has character that is not allowed in the alphabet.'
print(f'String: {testString}\nDFA: {dfaOutput}\nExpected: {expectedOutput}\n')