#This program is a game called "Mastermind"
import random
global puzzleLength
puzzleLength = 4

#main function
def main():

    #Initiate Variables
    colourList = [ 'red' , 'blue' , 'green']    #List of colours
    answerList = []                             #List of answers from user
    guesses = 0                                 #Counter for guesses
    solved = False                              #Default state of the game
    answerList = generateRandomColours(colourList)    #Generate the answers 

    #Sequences of functions for the game                                                 
    setup()                                     #Give instructions to teach users how to play
    while solved == False:
        userAnswer =getAnswer()                 #Function that gets user input
        guesses = countGuess(guesses)           #Function that keeps track the amount of guesses
        correctPosition = checkColours(answerList,userAnswer) #Function to analyse user input
        solved = isitSolved(correctPosition)    #Function to check whether the puzzle is solved
    print(f"Congratulations! You have solved the puzzle in {guesses} steps.")
    


    


###
###Function definitions here
###

#Print instructions to teach users how to play
def setup():
    print("Welcome to Mastermind!")  
    print(f"To win, guess the random generated sequence of {puzzleLength} colours in correct order.")
    print("Give your answer comma-seperated, like the following:")
    print("red,green,blue,red")
    

#Function to generate random colours and store into rColourList
def generateRandomColours(colourList):
    rColourList= []                       # Empty list of random colours
    for _i in range(puzzleLength):                          
        rColour = random.choice(colourList)
        rColourList.append(rColour)
    return rColourList


#Function to get answer/input from user
def getAnswer():
    
    while True: 
        answerList= []              #Empty list to store answers
        validAnswerList=[]            #Empty list to store answer that are str only
        answer = input("Answer:")   #Gets user input
        answer = answer.lower()     #Convert user input to lowercase
        answerList = answer.split(sep=',') #Convert user input from string to list
        
        
        #Answer checks/filtering
        if answer.count(',')< puzzleLength:         #checks for extra ',' given from user
            
            #Input validation and converting answer from str -> list
            for i in answerList: 
                if i.isdigit() == False  and i=='red' or i=='green' or i=='blue':
                    validAnswerList.append(i)
                else:
                    print("Input incorrect. Please check spelling and try again.")
                    break
            
            #Validation checks to answerList
            if  len(validAnswerList) == puzzleLength:     #Sufficient valid inputs 
                break
            elif len(validAnswerList) > puzzleLength:     #Too many arguments case
                print("Too many arguments. Please try again")
            elif len(validAnswerList) < puzzleLength and len(answerList)!= puzzleLength:  #Too little arguments case
                print("Too little arguments. Please try again")
        else:
            print("Too many arguments or extra comma found. Please try again")

    return validAnswerList
    

#Function to keep track the number of guesses
def countGuess(guesses):
    guesses +=1
    return guesses


#Function to check how many colours the user got correct
def checkColours(answerList,userAnswer):
    correctColours = 0
    # correct answers with N + colour
    Nred = answerList.count('red')
    Nblue = answerList.count('blue')
    Ngreen = answerList.count('green')
    # user input with small n + colour
    nred = userAnswer.count('red')
    nblue = userAnswer.count('blue')
    ngreen = userAnswer.count('green')
    #The case where the user has more Reds than the actual answer
    if nred >= Nred:         
        cred = Nred
    else:
        cred = nred
    #The case where the user has more Blue than the actual answer
    if nblue > Nblue:         
        cblue = Nblue
    else:
        cblue = nblue
    #The case where the user has more Green than the actual answer
    if ngreen > Ngreen:         
        cgreen = Ngreen
    else:
        cgreen = ngreen
    #Now we have amount of colours the user guessed correctly
    correctColours = cred + cgreen + cblue

# Now we analyse the number of correctly guessed positions of colours
    correctPositions = 0
    for i in range(len(answerList)):
        if answerList[i] == userAnswer[i]:
            correctPositions += 1
    if correctPositions == 4:
        pass
    else:
     print(f"Correct colour in the correct place: {correctPositions}")
     print(f"Correct colour but in the wrong place: {correctColours - correctPositions}")
    
    return correctPositions


#function to check whether the user managed to guess the answer correctly
def isitSolved(correctPositions):
    if correctPositions == puzzleLength:
        return True
    else:
        return False
    




if __name__ == "__main__":
    main()