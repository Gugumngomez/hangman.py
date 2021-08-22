import random 

name = input("What's your name? ")
print("Hello " + name + " Let's play hangman")

words = ["gorilla", "flamingo", "lion", "rhino", "hippo", "bear"]
random_word = random.choice(words)

print("Guess the letters")
guesses = " "
turns = 6

while turns > 0:
    fail = 0

    for char in random_word:

        if char in guesses:
            print(char)
        else:
            print("_")
            fail += 1
        if fail == 0:
            print("Correct")
            print("The word is", random_word)
            break
        guess = input("Guess a letter:")

        guesses += guess

        if guess not in random_word:
            turns -= 1
            print("Incorrect")

            if turns == 0:
                print("you lost")
