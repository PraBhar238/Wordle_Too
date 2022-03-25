from english_words import english_words_lower_alpha_set
# A non standard python library for random english words used to get random 5 letter words in the game.

class Wordle_Too:
    def __init__(self,Player_profile1,Player_profile2):
        self.Player_profile1 = Player_profile1
        self.Player_profile2 = Player_profile2
        self.x = 0
        self.chances = 0
        self.player_score = 0
        self.guess_word = ''
        self.The_Actual_List = ''
# Class Objects initialiser other than the first two all others are used locally by the program.

    def Get_Guess(self):
        if self.Player_profile2 == 'c' or 'C':
            for i in english_words_lower_alpha_set:
                if len(i) == 5:
                    self.guess_word = i
                    self.The_Actual_List = [char for char in self.guess_word]
                    return self.guess_word
# Random 5 letter word picker from the imported library and converts string into a list to compare individual letters.

    def Actual_Wordle(self):
        if self.Player_profile2 == 'c':
            self.chances += 6
            print('\nA 5 letter word has been chosen for you guess it in ' + str(self.chances) + ' chances')
        elif self.Player_profile2 == 'C':
            self.chances += 5
            print('\nA 5 letter word has been chosen for you guess it in ' + str(self.chances) + ' chances')
# Input chances determining algorithm. Based on game mode selection by the user.

        #print(self.guess_word) #This is a debug and build tool which can also work as a cheat code ;)
        while self.x < self.chances:
            The_Answer = input()
            Also_Actual = [char for char in The_Answer]
            print('+' + '=' * 40 + '+')
# User guess input and string to list converter

            for i in range(len(self.The_Actual_List) and len(The_Answer)):
                if The_Answer[i] == self.The_Actual_List[i]:
                    print(The_Answer[i], True)
                elif The_Answer[i] in self.The_Actual_List:
                    print(The_Answer[i], 'Maybe')
                else:
                    print(The_Answer[i], False)
            self.x += 1
# Input chance script. The chance numbers are determined by an earlier code above

            if Also_Actual[:] == self.The_Actual_List[:]:
                print('Congratulations!!, You did it in ' + str(self.x) + ' tries')
                print('The given word was: '+str(self.The_Actual_List))
                break
            else:
                print('You have ' + str(self.chances - self.x) + ' tries remaining')
                if self.x >= self.chances:
                    print('You lost!, The given word was: '+str(self.The_Actual_List))
# Checker for if all the letters are equal to the guess word letters are not and ouputs result based on it.

# The actual game function, creates a chance mechanism based on mode selection by the user, takes input from user and
# converts to list, compares the generated word list with the user input list and outputs result based on it.
# If all comparisions are True then the match is won.

    def Score_Calc(self):
        self.player_score = 0
        chance_remaining = self.chances - self.x + 1
        if self.Player_profile2 == 'C':
            self.player_score = 100 + (chance_remaining * 80)
        else:
            self.player_score = 20 + (chance_remaining * 80)

        self.player_score = (self.player_score / 500 * 100)
        return self.player_score
# An algorithm made for calculating score based on user play and mode selection.

    def Report(self):
        print('\n+' + '=' * 40 + '+')
        print('Player name: ',self.Player_profile1)
        print('Difficulty: ',self.Player_profile2)
        print('Final score: ',self.player_score,'%')
        print('+' + '=' * 40 + '+')
# A complete report of the game session of a user.

input('\nThe game is still in developmental stages so there are still some unsolved issues such as:'
      '\n ! Anything over 5 letters will crash the game as input validation isnt built in'
      '\n ! Have to load the game from system as play loop isnt built yet'
      '\n * Upcoming updates will include new gamemode, some bug fixes and a retro GUI '
      'Press enter to start game: ')
# Some warnings and game data.

Begin_Wordle = Wordle_Too(Player_profile1=input('\nPlease enter your name here\n'),
                          Player_profile2=input('\nSelect game mode by respective keystroke:'
                                                '\n* Casual <c> \n* Competitive <C>\n'))
# Takes the 2 inputs from the user required by class obejcts.

Begin_Wordle.Get_Guess()
Begin_Wordle.Actual_Wordle()
Begin_Wordle.Score_Calc()
Begin_Wordle.Report()
# Game initialiser and subsequents play.