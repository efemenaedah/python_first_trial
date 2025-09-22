#Write a program in python that will simulate the function of the Fortune cookie 
# we have to import the random module
import random
#lets declare the min and max number
min = 1
max = 99
#Lets declare variable to start the loop
open_cookie = "yes"
#start the while loop to run the program
while open_cookie == "yes":
    print("Breaking your cookie")

    #Declaring the lottery numbers to the random module
    lottery_number = (random.randint(min,max))
    print("your cookie reveals" , lottery_number)
    #create variable for sets of 4 random numbers 
    random_numbers = random.sample(range(min,max), 4)
    print(random_numbers)

    #creating a list of random fortunes
    fortune = ["your patner will approach you today", "you will be successful", "you are winning a million dollars next month", "A small risk taken will ripple into a big reward", "you will be an engineer someday", "people will know you for something great"]
    #creating variable for a random fortune 
    random_fortune = (random.choice(fortune))
    print(random_fortune,)
    #setting a variable to determine if we need to keep breaking our cookie
    open_cookie = input("open_cookie?")



