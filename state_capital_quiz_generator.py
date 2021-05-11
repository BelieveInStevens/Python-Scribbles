#! python3
# state_capital_quiz_generator - Creates enough quizzes on state capitals for the class

import os
import random 


os.chdir('c:\\Users\\stevend\\Documents\\Python Scripts\\Quizzes')

capitals = {'Alabama': 'Montgomery', 
'Alaska': 'Juneau', 
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 
'California': 'Sacramento', 
'Colorado': 'Denver',
'Connecticut': 'Hartford', 
'Delaware': 'Dover', 
'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 
'Hawaii': 'Honolulu', 
'Idaho': 'Boise', 
'Illinois':'Springfield', 
'Indiana': 'Indianapolis', 
'Iowa': 'Des Moines', 
'Kansas':'Topeka', 
'Kentucky': 'Frankfort', 
'Louisiana': 'Baton Rouge', 
'Maine':'Augusta', 
'Maryland': 'Annapolis', 
'Massachusetts': 'Boston', 
'Michigan':'Lansing', 
'Minnesota': 'Saint Paul', 
'Mississippi': 'Jackson', 
'Missouri':'Jefferson City', 
'Montana': 'Helena', 
'Nebraska': 'Lincoln', 
'Nevada':'Carson City', 
'New Hampshire': 'Concord', 
'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 
'New York': 'Albany', 
'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 
'Ohio': 'Columbus', 
'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 
'Pennsylvania': 'Harrisburg', 
'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 
'South Dakota': 'Pierre', 
'Tennessee':'Nashville', 
'Texas': 'Austin', 
'Utah': 'Salt Lake City', 
'Vermont': 'Montpelier', 
'Virginia': 'Richmond', 
'Washington': 'Olympia', 
'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 
'Wyoming': 'Cheyenne'}


# Generate 35 quiz files
for quiz_num in range(2):
    # Create the quiz and it's answer key.
    quiz_file = open('capitalsquiz%s.txt' % (quiz_num + 1), 'w')
    answer_key_file = open('capitalsquiz_answers%s.txt' % (quiz_num + 1), 'w')

    # Create the Quiz header.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' \
        %  (quiz_num + 1))
    quiz_file.write('\n\n')

    # Create a random ordering of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states and generate a question for each.
    for question_num in range(50):

        # Get Correct and Incorrect Answers
        correct_answer = capitals[states[question_num]]
        wrong_answers = random.sample(list( 
            filter(lambda x: x != correct_answer, capitals.values())), 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
    
        # Write the questions and answer options to the quiz file.
        quiz_file.write('%s. What is the capital of %s?\n' \
            % (question_num + 1, states[question_num]))
        for i in range(4):
            quiz_file.write('    %s. %s\n' % ('ABCD'[i], answer_options[i]))
        quiz_file.write('\n')

        # Write the answers to the answer key file.
        answer_key_file.write('%s. %s\n' % (question_num + 1, \
            'ABCD'[answer_options.index(correct_answer)]))
    quiz_file.close()
    answer_key_file.close()


