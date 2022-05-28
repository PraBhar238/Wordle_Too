import stdiomask
from getpass import getpass
from english_words import english_words_lower_alpha_set
# importing all the required libraries for masking input in coop and english words respectively.

print('\nWelcome, to the game : '
'\n\n\t██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗     ████████╗ ██████╗  ██████╗'
'\n\t██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝     ╚══██╔══╝██╔═══██╗██╔═══██╗'
'\n\t██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗          ██║   ██║   ██║██║   ██║'
'\n\t██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝          ██║   ██║   ██║██║   ██║'
'\n\t╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗███████╗██║   ╚██████╔╝╚██████╔╝'
'\n\t ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝    ╚═════╝  ╚═════╝ *\n')
# Fancy word art for game banner.

print('Rules of the game : \n> Only enter small letter words, no numerals or characters.'
      '\n> Both game modes only have 6 chances and 5 letter inputs. \n [*]Good Luck[*]')
# Rules and regulations output.

class Wordle_Too:
    def __init__(self, Player_profile1, Player_profile2):
        self.Player_profile1 = Player_profile1
        self.Player_profile2 = Player_profile2
        self.x = 0
        self.chances = 0
        self.player_score = 0
        self.guess_word = ''
        self.The_Actual_List = ''
# initialising all the datas required for the computer mode class.

    def Get_Guess(self):
        if self.Player_profile2 == 'c':
            for i in english_words_lower_alpha_set:
                if len(i) == 5:
                    self.guess_word = i
                    self.The_Actual_List = [char for char in self.guess_word]
                    return self.guess_word
# Code for only taking 5 letter words from the english words library and converting string to char array.

    def Actual_Wordle(self):
        if self.Player_profile2 == 'c':
            self.chances += 6
            print('\nA 5 letter word has been chosen for you guess it in ' + str(self.chances) + ' chances')
# Creates chances for the player and outputs remaining chances after each loop.

        # print(self.guess_word) #This is a debug and build tool which can also work as a cheat code :)
        while self.x < self.chances:
            The_Answer = input()
            if len(The_Answer) != 5:
                while len(The_Answer) != 5:
                    The_Answer = input('--Error--Please input a valid 5 letter word only : ')
            Also_Actual = [char for char in The_Answer]
            print('+' + '=' * 40 + '+')
# Input validation and error handling for each chance.
 
            for i in range(len(self.The_Actual_List) and len(The_Answer)):
                if The_Answer[i] == self.The_Actual_List[i]:
                    print(The_Answer[i], True)
                elif The_Answer[i] in self.The_Actual_List:
                    print(The_Answer[i], 'Maybe')
                else:
                    print(The_Answer[i], False)
            self.x += 1
# Compare input and given word.

            if Also_Actual[:] == self.The_Actual_List[:]:
                print('\nCongratulations!!, You did it in ' + str(self.x) + ' tries')
                print('\nThe given word was: ' + str(self.The_Actual_List))
                break
            else:
                print('\nYou have ' + str(self.chances - self.x) + ' tries remaining')
                if self.x >= self.chances:
                    print('\nYou lost!, The given word was: ' + str(self.The_Actual_List))
# If all the compares are proper then the game is won and respective player data is outputted here.

    def Report(self):
        print('\n+' + '=' * 40 + '+')
        print('Player name: ', self.Player_profile1)
        print('Game mode: ', self.Player_profile2)
        print('Total attempts: ', self.x)
        print('+' + '=' * 40 + '+')
# Output all the player data after the game is finished.

Player_profile1 = input('\nPlease enter your name here : ')
while len(Player_profile1) < 1:
    Player_profile1 = input('Please enter a valid name : ')
# Take and store player name.

Player_profile2 = input('\nSelect game mode by respective keystroke:\n* Computer : [Guess word chosen by computer] <c> \n* Co-Op    : [Guess word chosen by friend]   <C> \n')
# Mode select and store.

Begin_Wordle = Wordle_Too(Player_profile1, Player_profile2)

if Player_profile2 == 'c':
    Begin_Wordle.Get_Guess()
    Begin_Wordle.Actual_Wordle()
    Begin_Wordle.Report()

elif Player_profile2 == 'C':
# Based on player game mode input the script runs for respective mode. 

    def GuessInput():
        PlayerInput = stdiomask.getpass('\nEnter the 5 letter word here for the other person to guess : ')
        while len(PlayerInput) != 5:
            PlayerInput = stdiomask.getpass('--Error--\nPLease enter only a 5 letter word : ')
        alsoPlayerInput = [char for char in PlayerInput]
# Take input from a player and mask while converting it from string to char array.

        print('\nA 5 letter word has been given')
        x = 0
        while x < 6:
            AnswerInput = input('Enter the 5 letter word of your guessing here : ')
            if len(AnswerInput) != 5:
                while len(AnswerInput) != 5:
                    AnswerInput = input('--Error--\nPlease input a valid 5 letter word only : ')
            alsoAnswerInput = [char for char in AnswerInput]
            print('+' + '=' * 40 + '+')

            for i in range(len(alsoPlayerInput) and len(AnswerInput)):
                if AnswerInput[i] == alsoPlayerInput[i]:
                    print(AnswerInput[i], True)
                elif AnswerInput[i] in alsoPlayerInput:
                    print(AnswerInput[i], 'Maybe')
                else:
                    print(AnswerInput[i], False)
            x += 1
# The entire sequence for taking player input in given amount of chances check for error and convert to char array.

            if alsoAnswerInput[:] == alsoPlayerInput[:]:
                print('Congratulations you WON, in only ' + str(x) + ' tries')
                print('\n+' + '=' * 40 + '+')
                print('Player name: ', Player_profile1)
                print('Game mode: ', Player_profile2)
                print('Total attempts: ', x)
                print('+' + '=' * 40 + '+')
                break
            elif x >= 6:
                print('You lost, You have 0 chances \nThe given word was [' + PlayerInput + ']')
            else:
                print('Try again you have ' + str(6 - x) + ' chances remaining')
# Check for if all the inputs are correct and output message andd respective data.


    GuessInput()

Good_Bye = input('Press any key to exit : ')
# Game exit sequence.
