# writing a code to simulate The Magic 8 Ball game used for fortune-telling or seeking advice
# we import the random Module:
import random
# we declare the variables for Answers to questions
Answers =  ["it is certain", "Yes definitely", "Most Likely", "Yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Dont count on it", "my reply is No", "Outlook not so good", "Very doubtful"]
#variable to keep loop running
Ask_questions = "spin"
while Ask_questions == "spin": 
    # let users know what activity to do next
    print("spinning the ball" )
    #Declaring the ball answers to the random module
    Ball_answer = (random.choice(Answers))
    #print the value of the response
    print(Ball_answer)
    Ask_questions = input("Ask_questions here")