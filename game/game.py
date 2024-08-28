import random

while True:
    try:
        level = int(input("Level: "))
        number = random.randint(1, level)
        while True:
            user_guess = int(input("Guess: "))
            if user_guess > number:
                print("Too large!")
            elif user_guess < number:
                print("Too small!")
            elif user_guess == number:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
