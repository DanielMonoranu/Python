from random_words import RandomWords
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

random_word = RandomWords()
word = str(random_word.random_words()[0])
# print(word2)

end_of_game = False
lives_counter = 7
display = []
for i in range(0, len(word)):
    display += "-"
print("HANGMAN")

while end_of_game != True:
    guess_letter = input("Guess a letter: ")

    for position in range(len(word)):
        letter = word[position]
        if letter == guess_letter:
            display[position] = letter

    if "-" not in display:
        end_of_game = True
        print("You win!")

    if guess_letter not in word:
        lives_counter -= 1
        print(stages[lives_counter])

    if lives_counter == 0:
        print(f"You lose! The word is {word}.")
        break

    print(display)
