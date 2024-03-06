#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

// Define alphabet (sigma) 
const string alphabet = "abcdefghijklmnopqrstuvwxyz";

/*
  Define start and accept states.
  Define accept state that will be later comapred to the current state (accepts if matches).
*/
string startState = "q0";
string acceptingState = "q11";

/*
Define transitions.

otherwiseTransitionState: state where the current state goes to with otherwise (referece DFA Diagram)
customTransitions: transitions where current state goes to different state that the sigma does not go to (referece DFA Diagram)
*/
unordered_map<char, string> createTransition(
  const string& otherwiseTransitionState, 
  const unordered_map<char, string>& customTransitions = {}
) {
    unordered_map<char, string> transitions;
    for (char letter : alphabet) {
        if (customTransitions.find(letter) != customTransitions.end()) {
            transitions[letter] = customTransitions.at(letter);
        } else {
            transitions[letter] = otherwiseTransitionState;
        }
    }
    return transitions;
}

// Define DFA states and transitions for each state
unordered_map<string, unordered_map<char, string>> statesAndTransitions = {
    {"q0", createTransition("q0", {{'k', "q1"}})},
    {"q1", createTransition("q0", {{'h', "q2"}, {'k', "q1"}})},
    {"q2", createTransition("q0", {{'i', "q3"}, {'k', "q1"}})},
    {"q3", createTransition("q0", {{'k', "q1"}, {'r', "q4"}})},
    {"q4", createTransition("q0", {{'b', "q5"}, {'k', "q1"}})},
    {"q5", createTransition("q0", {{'k', "q1"}, {'y', "q6"}})},
    {"q6", createTransition("q6", {{'c', "q7"}})},
    {"q7", createTransition("q6", {{'a', "q8"}, {'c', "q7"}})},
    {"q8", createTransition("q6", {{'c', "q7"}, {'l', "q9"}})},
    {"q9", createTransition("q6", {{'c', "q7"}, {'m', "q10"}})},
    {"q10", createTransition("q6", {{'c', "q7"}, {'a', "q11"}})},
    {"q11", createTransition("q11")}
};

// Create and visualize the DFA
string khirbyCalmaDFA(
  const unordered_map<string, unordered_map<char, string>>& statesAndTransitions, 
  const string& startingState,
  const string& acceptingState,
  const string& testString
) {
    // Set current state to start state at the beginning since that is where the beginning of the string begins.
    string currentState = startState;
    /*
      Go though each letter in string.
      Update current state based on the current state's defined transition of the current letter.
      Also checks if current letter is valid via lowercase alphabet. If not valid, error.
    */
    for (char letter : testString) {
        if (alphabet.find(letter) == string::npos) {
            return "Error: String has character that is not allowed in the alphabet.";
        } else {
            currentState = statesAndTransitions.at(currentState).at(letter);
        }
    }
    /*
      Finishes going through whole string.
      Check if current state (once the DFA went through the whole string) matches with the defined accepting state.
    */
    if (currentState == acceptingState) {
        return "Accept";
    } else {
        return "Reject";
    }
}

// Automatically runs through each string test case and prints out the result
void runTestCases() {
    // Test cases (to add more test cases, include the strings within the testStrings vector)
    vector<string> testStrings = {
        "khirbycalma",
        "dsfsuyfbqbidskkhirbycalma",
        "khirbydfigufdguibdfvccalma",
        "khirbycalmaaciuerafbdskjfb",
        "sdifhsuifsakkhirbysdofsofsoojccalmaaciuerafbdskjfb",
        "khikhirbycalma",
        "khirbycalcalma",
        "",
        "kirbycalma",
        "khirbycalm",
        "&khirbycalma",
        "khirbyKcalma",
        "khirbycalmaC"
    };
    // Run each string test case and print its output from the DFA
    for (const string& testString : testStrings) {
        string dfaOutput = khirbyCalmaDFA(statesAndTransitions, startState, acceptingState, testString);
        cout << "Test String: " << testString << "\nDFA: " << dfaOutput << "\n\n";
    }
}

int main() {
    runTestCases();
    return 0;
}