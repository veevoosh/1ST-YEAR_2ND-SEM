def login():
    username = "Radio_Star_1933"
    password = "What_Is_A_Password_???"
    attempts = 3

    while attempts != 0:
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")

        if input_username == username and input_password == password:
            print("\n"
                  "> Welcome,", username.capitalize() + "! \n")
            print("Profile: \n"
                  "\t Radio_Star_1933 \n"
                  "\n"
                  "Public Posts: \n"
                  "\t Radio_Star_1933 (03/01/2024 - 4:25pm) \n"
                  "\t > Test \n"
                  "\n"
                  "\t Radio_Star_1933 (03/01/2024 - 4:27pm) \n"
                  "\t > Hello. How do you use this website . \n"
                  "\n"
                  "\t Radio_Star_1933 (03/01/2024 - 4:28pm) \n"
                  "\t > hbfjisjkdfmjnbfksdlmvn mv, vfl \n"
                  "\n"
                  "\t Radio_Star_1933 (03/01/2024 - 4:30pm) \n"
                  "\t > Apologies for the last post. \n"
                  "\t > I accidentally spilled coffee all over my keyboard. \n"
                  "\t > So, I had to wipe it off. \n"
                  "\t > I did not realize it would actually post. Whoops.")
            exit()
        else:
            attempts -= 1
            if attempts > 0:
                print("> Incorrect username or password. \n"
                      "> Please try again. \n")
                print("Attempts left:", attempts)
            if attempts == 0:
                print("> You have run out of attempts. \n"
                      "> Access denied.")
                return False

def main():
    print("Welcome to the Chirper Login System!")
    if login() is False:
        print("> Your account is blocked.")
        exit()
    if __name__ == "__main__":
        main()

main()
