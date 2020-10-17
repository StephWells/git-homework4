#Create a function that randomly generates and returns a tuple of two positive one-digit integers. 
#Then prompt the user for the multiplication of the two numbers. 
#For example, if the generated number is 3 and 7, the prompt message is  
#How much is 3 times 7? 
#Then compare the user answer with the correct result. If the answer is correct, display a message “done”. 
#Otherwise, if the user input 20, prompt: “3 times 7 is not 20, please try again: “
#Keep asking the user input until it type the correct answer.

import random

def generateRan():
    randomDigit1 = random.randint(1,9)
    randomDigit2 = random.randint(1,9)
    correctAnswer = randomDigit1 * randomDigit2
    userAnswer = int(input(f'How much is {randomDigit1} times {randomDigit2} ?'))
    if userAnswer == correctAnswer:
        print('done')
    else:
        print(randomDigit1, 'times', randomDigit2, 'is not', userAnswer, ", please try again:")
generateRan()    