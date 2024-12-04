import random

print("* UEE HEE HEE! \n"
      "\n"
      "* WELCOME, TRAVELER, TRAVELER! \n"
      "* TO THE NUMBER GUESSING GAME, GAME! \n"
      "\n"
      "* THE RULES ARE SIMPLE, SIMPLE! \n"
      "* GUESS MY SECRET NUMBER CORRECTLY, AND YOU WIN, WIN!")

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("\n Enter your guess (1-100): "))
        attempts += 1

        if guess < secret_number and attempts != 5:
            print("\n"
                  "* UEE HEE HEE! THAT IS TOO LOW, LOW! \n"
                  "* TRY AGAIN, AGAIN!")
        elif guess > secret_number and attempts != 5:
            print("\n"
                  "* UEE HEE HEE! THAT IS TOO HIGH, HIGH! \n"
                  "* TRY AGAIN, AGAIN!")
        elif guess != secret_number and attempts == 5:
            print(f"\n"
                  f"* TOO BAD! YOU LOSE, LOSE!"
                  f"\n"
                  f"* YOU HAVE USED ALL YOUR 5 ATTEMPTS! \n"
                  f"* THE SECRET NUMBER WAS {secret_number}!")
            break
        else:
            print(f"\n"
                  f"* UEE HEE HEE! YOU WIN, YOU WIN!"
                  f"\n"
                  f"* YOU HAVE GUESSED THE NUMBER {secret_number} \n"
                  f"* IN {attempts} ATTEMPTS, ATTEMPTS!")
            break

def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        guess_number()
        play_again = input("* WELL, THEN... WOULD YOU LIKE TO PLAY AGAIN, AGAIN? \n"
                           "(YES/NO): ")

    print("\n"
          "* UEE HEE HEE! \n"
          "* VERY WELL! \n"
          "* UNTIL NEXT TIME, TRAVELER, TRAVELER!")

if __name__ == "__main__":
    main()
