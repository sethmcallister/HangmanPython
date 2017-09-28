import random;

words = ["cat", "dog", "elephant", "car", "bird"]
lives = 10;
correct = [];
word = words[random.randint(0, len(words))]

def askForGuess():
    character = input("please make a guess");
    makeAGuess(character);

def makeAGuess(character):
    global lives;

    if(word.__contains__(character)):
        if(correct.__contains__(character)):
            print("You have already guessed this character, please try again.");
            print("Correct guesses:", correct);
            askForGuess();
            return;
        print("You have guessed correctly, please guess again");
        correct.append(character);

        if(len(correct) == len(word)):
            print("You have guesses the word, it was", word);
            return;

        askForGuess();
        return;

    if lives == 0:
        print("You have run out of lives");
        return;
    print("Wrong guess, please try again");
    lives -= 1;
    print("You have", lives, "remaning")
    askForGuess();

print("The length of the word is", len(word))

askForGuess();
