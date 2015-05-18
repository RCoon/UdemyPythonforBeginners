# unit_3_review_quiz.py
# Written for Python 3.4.2
# Revision date: 4/26/15

# By: Ryan Coon

#-----------------------------------------------------------------------
# This program prints definitions of vocabulary words and asks the user
# to enter the matching word.  The program will end after a user-defined
# number of correct answers, and it will calculate their score.
#-----------------------------------------------------------------------

import random

# Introduces the program and its purpose to the user.
print('This program will print definitions of vocabulary words and ask you ')
print('to enter the matching word.\n')

# Assign the variable "definitions" to a dictionary with each vocabulary
# word as the key and its definition as the value.
definitions = {
'algorithm':'A general process for solving a category of problems.',
'bug':'An error in a program.',
'byte code':'An intermediate language between source code and object code.',
'compile':'To translate a program written in a high-level language into a '
'low-level language all at once, in preparation for later execution.',
'debugging':'The process of finding and removing any of the three kinds of '
'programming errors.',
'exception':'Another name for a runtime error.',
'executable':'Another name for object code that is ready to be executed.',
'formal language':'Any one of the languages that people have designed for '
'specific purposes, such as representing mathematical ideas or computer '
'programs; all programming languages are this kind of language.',
'high-level language':'A programming language like Python that is designed '
'to be easy for humans to read and write.',
'interpret':'To execute a program in a high-level language by translating it '
'one line at a time.',
'low-level language':'A programming language that is designed to be easy for a '
'computer to execute; also called machine language or assembly language.',
'natural language':'Any one of the languages that people speak that evolved '
'naturally.',
'object code':'The output of the compiler after it translates the program.',
'parse':'To examine a program and analyse the syntactic structure.',
'portability':'A property of a program that can run on more than one kind of '
'computer.',
'print statement':'An instruction that causes the Python interpreter to '
'display a value on the screen.',
'problem solving':'The process of formulating a problem, finding a solution, '
'and expressing the solution.',
'program':'A sequence of instructions that specifies to a computer actions and '
'computations to be performed.',
'Python shell':'An interactive user interface to the Python interpreter.',
'runtime error':'An error that does not occur until the program has started to '
'execute but that prevents the program from continuing.',
'script':'A program stored in a file (usually one that will be interpreted).',
'semantic error':'An error in a program that makes it do something other than '
'what the programmer intended.',
'semantics':'The meaning of a program.',
'source code':'A program in a high-level language before being compiled.',
'syntax':'The structure of a program.',
'syntax error':'An error in a program that makes it impossible to parse -- and '
'therefore impossible to interpret.',
'token':'One of the basic elements of the syntactic structure of a program, '
'analagous to a word in a natural language.',
'assignment statement':'A statement that assigns a value to a name (variable).', 'comment':'Information in a program that is '
'meant for other programmers (or anyone reading the source code) and has no '
'effect on the execution of the program.',
'composition':'The ability to combine simple expressions and statements into '
'compound statements and expressions in order to represent complex '
'computations concisely.',
'concatenate':'To join two strings end-to-end.',
'data type':'A set of values.',
'evaluate':'To simplify an expression by performing the operations in order '
'to yield a single value.',
'expression':'A combination of variables, operators, and values that '
'represents a single result value.',
'float':'A Python data type which stores floating-point numbers.',
'int':'A Python data type that holds positive and negative whole numbers.',
'integer division':'An operation that divides one integer by another and '
'yields an integer.',
'keyword':'A reserved word that is used by the compiler to parse programs.',
'operand':'One of the values on which an operator operates.',
'operator':'A special symbol that respresents a simple computation like '
'addition, multiplication, or string concatenation.',
'rules of precedence':'The set of rules governing the order in which '
'expressions involving multiple operators and operands are evaluated.',
'statement':'An instruction that the Python interpreter can execute.',
'str':'A Python data type that holds a string of characters.',
'value':'A number or string (or other things to be named later) that can be '
'stored in a variable or computed in an expression.',
'variable':'A name that refers to a value.',
'variable name':'A name given to a variable.'}

length = len(definitions)

# Obtain a positive integer greater than 1 from the user.
while True:
        # Assign the variable "max_tries" to the user-defined number of
        # correct guesses until the program ends.
        try:
            max_tries = int(input('There are {0} vocabulary words.  How many '
                                 'correct answers do you want to give before'
                                 ' the program quits?\n> '.format(length)))
        except ValueError:
            print("That's not an int!")
            continue
        else:
            if max_tries < 1:
                print("Enter 1 or greater.")
                continue
            else:
                break
            
count = 0
num_correct = 0
num_incorrect = 0
num_tries = 0

print('Possible answers are listed below.\n')

# Print out a list of all keys in the definitions dictionary sorted
# alphabetically, with spacing characters between each key
for key in sorted(definitions.keys(), key=str.lower):
    print(key,' | ', end="")

print('\n')
        
print('The program will end after you have given {0} correct answers.'
      .format(max_tries))
print('You can also end the program by typing Ctrl-D\n')

# Continue asking questions until the user has been asked max_tries
# questions.
while count < max_tries:
    # Assign the variable "word" to a random key in the
    # definitions dictionary.
    word = random.choice(list(definitions.keys()))
    # Assign the variable "definition" to the value associated with
    # the randomly chosen key above
    definition = definitions[word]
    print('Definition: ', definition,'\n')
    answer = input('What is the matching concept?\n> ')
    num_tries += 1
    if answer == word:
        count += 1
        num_correct += 1
        print("That's correct! You've answered {0} correctly.\n"
              .format(num_correct))
        tries_left = max_tries - num_tries
        # If there are more terms in the dictionary than the number of
        # tries the user has left, and the user has correctly matched
        # the definition with the word, remove that key:value from the
        # dictionary to avoid asking the user the same question.
        if len(definitions) > tries_left:
            del definitions[word]
    else:
        print('That is incorrect.  The answer is:', word,'\n')
        num_incorrect += 1
        continue
        

score = 100 * (num_correct / num_tries)


if num_incorrect == 0:
    print("You didn't miss any!  Looks like you're ready for the quiz.")
elif num_incorrect == 1:
    print('You only missed 1.  Not too shabby.')
else:
    # Display the amount of questions the user guessed correctly and
    # incorrectly.  Display the score with only 2 decimal places.
    print('You got {0} right and missed {1}.  Your score was '
          '{number:.{digits}f}%'.format(num_correct, num_incorrect,
                                        number=score, digits=2))