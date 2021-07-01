import random

category = input("Select your favorite category(by number)\n 1.Food \n 2.States of India \n 3.cartoon \n 4.Random \n")
if category == '1':
    words_list = ['pizza','fries','chicken fry','burger','biriyani']
elif category == '2':
    words_list = ['kerla','tamil nadu','karnataka','goa','delhi']
elif category == '3':
    words_list = ['doremon', 'dora', 'noddy', 'micky', 'shinchan', 'spider man']
elif category == '4':
    words_list = ['corona','doctor','happy','bottel','television']
else:
    print("unknow catogory,try again by choosing the right one from the menu,THANK YOU.")


word = random.choice(words_list)
winning_word = word
print(word)

word_length = len(word)
space = ["_"] * word_length
print(space)


def letter_position(guess, word, space):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            word = word[:index] + '*' + word[index + 1:]
            space[index] = guess
        else:
            index = -1
    return (word, space)


def win_check():
    for i in range(0, len(space)):
        if space[i] == '_':
            return -1

    return 1


lives = len(word)
for i in range(0, lives):
    guess = input("Enter your guess: ")
    if guess == winning_word:
        print("Your great you guessed the word..Congrats YOU WON ..!!!")
        break
    if guess in word:
        word, space = letter_position(guess, word, space)
        print(space)
    else:
        print("Sorry your guess is wrong  :(")

    if win_check() == 1:
        print("congratulations you won :) ")
        break

    print(" you have " + str(lives - i) + " turns left ")
    print()
