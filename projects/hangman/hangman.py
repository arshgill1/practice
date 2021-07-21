import random
from words import word_list

# get the word from list
def get_word():
    word = random.choice(word_list)   # randomly generate a word from the sequence word_list
    return word.upper()

def play(word):
    word_completion = "_" * len(word)  # empty spaces as per the length of the random word
    guessed = False
    # Create 2 lists one to hold letter guessed and one to hold word guessed
    guessed_letters = []
    guessed_words = []
    # no of tries available before you loose
    tries = 6
    # display initial things
    print(display_hangman(tries))
    print("Length of the word is", len(word), "letters")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        print("Remaining tries: ", tries)
        guess = input("Please guess the letter or word: ").upper()
        # 3 possible conditions
        if len(guess) == 1 and guess.isalpha():
            # checking if the letter is already in the word | not in the word | is in the word
            if guess in guessed_letters:
                print("You already guessed the letter.", guess)
                print("Remaining tries: ", tries)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries-=1
                print("Remaining tries: ", tries)
                guessed_letters.append(guess)   # storing and keeping the record of previous attempts
            else:
                print("Good job!", guess, "is in the word.")
                guessed_letters.append(guess)   # storing for future attempts that letter was already used.
                # update the variable word completion to reveal user of all occurrences of guess
                # for this convert string to list to be able to index into it
                word_as_list=list(word_completion)
                # find all indices where guess occurs in the word
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # for loop over indices to replace each _ with index to guess
                for index in indices:
                    word_as_list[index] = guess
                    # update word completion and convert back to string
                    word_completion = "".join(word_as_list)
                    # check if the guess completes the word
                    if "_" not in word_completion:
                        guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            # check if the word is already guessed, correct or incorrect
            if guess in guessed_words:
                print("You already guessed the word.", guess)
                print("Remaining tries: ", tries)
            elif guess != word:
                print(guess, "not in the word")
                tries-=1
                print("Remaining tries: ", tries)
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            # after each guess handled print current state of hangman and word
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, You guessed the word! You Win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    # get the word from get_word() and pass it to play()
    word = get_word()
    play(word)
    # Play again Option
    while input("Play Again? (Y/N)").upper() == "Y":
        word=get_word()
        play(word)

main()
