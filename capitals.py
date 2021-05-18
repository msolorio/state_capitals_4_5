import random

states = [
    {
        "name": "Alabama",
        "capital": "Montgomery"
    },
    {
        "name": "Alaska",
        "capital": "Juneau"
    },
    {
        "name": "Arizona",
        "capital": "Phoenix"
    }
]

answers = {}

"""
answers = {
    'Alabama': {
        'correct': 2,
        'incorrect': 3
    },
    'Alaska': {
        'correct': 1,
        'incorrect': 3
    }
}
"""

# PSEUDOCODE
# - WELCOME MESSAGE TO PLAYER
# - RANDOMIZE THE LIST OF OBJECTS
# - LOOP THROUGH LIST
# -- PROMPT THE USER: ASK FOR THE CAPITAL FOR THE GIVEN STATE
# -- AFTER USER SUBMITS THEIR ANSWER
# -- INCREMENT CORRECT/INCORRECT ANSWERS FOR THAT STATE
# - AFTER ALL STATES LOOPED THROUGH
# --ASK USER IF THEY WANT TO PLAY AGAIN




def print_welcome():
    print('''Welcome to State Guru: the state capitals guessing game
    ''')




def show_state_tally(state_name, state_tally, correct):
    print('===================================================')
    if correct:
        print('That is correct!')
    else:
        print('This is incorrect :(')

    print(f'Tally for {state_name}')
    print(f'Correct answers: {state_tally["correct"]}')
    print(f'Incorrect answers: {state_tally["incorrect"]}')
    print('===================================================')
    print('')




def loop_through_states():
    random.shuffle(states)

    for state in states:
        capital_response = input(f'What is the capital of {state["name"]}?\n')
        state_name = state['name']

        if state_name not in answers:
            answers[state_name] = {
                'correct': 0,
                'incorrect': 0
            }

        if capital_response == state['capital']:
            answers[state_name]['correct'] += 1
            show_state_tally(state_name, answers[state_name], True)
        else:
            answers[state_name]['incorrect'] += 1
            show_state_tally(state_name, answers[state_name], False)


    play_again_response = input('Would you like to play again? y/n\n')

    if play_again_response == 'y':
        loop_through_states()

    else:
        return




def get_correct_responses(answers):
    num_correct = 0

    for state_name, state_data in answers.items():
        num_correct += state_data['correct']

    return num_correct




def get_incorrect_responses(answers):
    num_incorrect = 0

    for state_name, state_data in answers.items():
        num_incorrect += state_data['incorrect']

    return num_incorrect




def print_score():
    # Print number of correct answers
    print(f'Total number of correct answers: {get_correct_responses(answers)}')
    # Print number of incorrect answers
    print(f'Total number of incorrect answers: {get_incorrect_responses(answers)}')



print_welcome()

loop_through_states()

print_score()

# print(answers)

# //////////////////////////////////////////////////////
# an array of state dictionaries
# states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery"
# }, {
#     "name": "Alaska",
#     "capital": "Juneau"
# }, {
#     "name": "Arizona",
#     "capital": "Phoenix"
# }, {
#     "name": "Arkansas",
#     "capital": "Little Rock"
# }, {
#     "name": "California",
#     "capital": "Sacramento"
# }, {
#     "name": "Colorado",
#     "capital": "Denver"
# }, {
#     "name": "Connecticut",
#     "capital": "Hartford"
# }, {
#     "name": "Delaware",
#     "capital": "Dover"
# }, {
#     "name": "Florida",
#     "capital": "Tallahassee"
# }, {
#     "name": "Georgia",
#     "capital": "Atlanta"
# }, {
#     "name": "Hawaii",
#     "capital": "Honolulu"
# }, {
#     "name": "Idaho",
#     "capital": "Boise"
# }, {
#     "name": "Illinois",
#     "capital": "Springfield"
# }, {
#     "name": "Indiana",
#     "capital": "Indianapolis"
# }, {
#     "name": "Iowa",
#     "capital": "Des Moines"
# }, {
#     "name": "Kansas",
#     "capital": "Topeka"
# }, {
#     "name": "Kentucky",
#     "capital": "Frankfort"
# }, {
#     "name": "Louisiana",
#     "capital": "Baton Rouge"
# }, {
#     "name": "Maine",
#     "capital": "Augusta"
# }, {
#     "name": "Maryland",
#     "capital": "Annapolis"
# }, {
#     "name": "Massachusetts",
#     "capital": "Boston"
# }, {
#     "name": "Michigan",
#     "capital": "Lansing"
# }, {
#     "name": "Minnesota",
#     "capital": "St. Paul"
# }, {
#     "name": "Mississippi",
#     "capital": "Jackson"
# }, {
#     "name": "Missouri",
#     "capital": "Jefferson City"
# }, {
#     "name": "Montana",
#     "capital": "Helena"
# }, {
#     "name": "Nebraska",
#     "capital": "Lincoln"
# }, {
#     "name": "Nevada",
#     "capital": "Carson City"
# }, {
#     "name": "New Hampshire",
#     "capital": "Concord"
# }, {
#     "name": "New Jersey",
#     "capital": "Trenton"
# }, {
#     "name": "New Mexico",
#     "capital": "Santa Fe"
# }, {
#     "name": "New York",
#     "capital": "Albany"
# }, {
#     "name": "North Carolina",
#     "capital": "Raleigh"
# }, {
#     "name": "North Dakota",
#     "capital": "Bismarck"
# }, {
#     "name": "Ohio",
#     "capital": "Columbus"
# }, {
#     "name": "Oklahoma",
#     "capital": "Oklahoma City"
# }, {
#     "name": "Oregon",
#     "capital": "Salem"
# }, {
#     "name": "Pennsylvania",
#     "capital": "Harrisburg"
# }, {
#     "name": "Rhode Island",
#     "capital": "Providence"
# }, {
#     "name": "South Carolina",
#     "capital": "Columbia"
# }, {
#     "name": "South Dakota",
#     "capital": "Pierre"
# }, {
#     "name": "Tennessee",
#     "capital": "Nashville"
# }, {
#     "name": "Texas",
#     "capital": "Austin"
# }, {
#     "name": "Utah",
#     "capital": "Salt Lake City"
# }, {
#     "name": "Vermont",
#     "capital": "Montpelier"
# }, {
#     "name": "Virginia",
#     "capital": "Richmond"
# }, {
#     "name": "Washington",
#     "capital": "Olympia"
# }, {
#     "name": "West Virginia",
#     "capital": "Charleston"
# }, {
#     "name": "Wisconsin",
#     "capital": "Madison"
# }, {
#     "name": "Wyoming",
#     "capital": "Cheyenne"
# }]
