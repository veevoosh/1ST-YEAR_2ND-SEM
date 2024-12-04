import datetime
import calendar


class Calendar_Utility:

    @staticmethod
    def find_weekday(self):
        try:
            user_year = int(input("Enter the year: "))
            user_month = int(input("Enter the number of the month: "))
            user_day = int(input("Enter the day of the month: "))
            user_date = f"{user_month}/{user_day}/{user_year}"
            weekday = calendar.weekday(user_year, user_month, user_day)
            print(f"\n>> The weekday for {user_date} is {weekday}.\n")

        except ValueError:
            print("\nSorry, that is an invalid input.\n"
                  ">> Please enter a valid date.\n")
            return

    def check_leap_year(self):
        try:
            user_date = int(input("\nEnter a year: "))
            leap = calendar.isleap(user_date)
            if leap:
                print(f">> The year {user_date} is a leap year.\n")
                return
            if not leap:
                print(f">> The year {user_date} is not a leap year.\n")
                return

        except ValueError:
            print("\nSorry, that is an invalid input.\n"
                  ">> Please enter a valid date.\n")
            return

    def generate_calendar(self):
        try:
            user_year = int(input("Enter a year: "))
            user_month = int(input("Enter a month: "))
            print()
            calendar.prmonth(user_year, user_month)
            print()
            return

        except ValueError:
            print("\nSorry, that is an invalid input.\n"
                  ">> Please enter a valid date.\n")
            return

    def iterate_dates(self):
        try:
            user_year = int(input("Enter the year: "))
            user_month = int(input("Enter the number of the month: "))
            user_day = int(input("Enter the day of the month: "))
            user_date = f"{user_month}/{user_day}/{user_year}"
            print()
            c = calendar.Calendar()
            print(f">> The list of dates for {user_date} are:")
            for date in c.itermonthdates(user_year, user_month):
                print(f">>>> {date}", end="\n")
            print()

        except ValueError:
            print("\nSorry, that is an invalid input.\n"
                  ">> Please enter a valid date.\n")
            return

    def run(self):
        while True:
            try:
                print("Welcome to the Calendar Function Demo!\n"
                      "\nWhat would you like to do?\n"
                      "[1] Determine the weekday for a given date\n"
                      "[2] Check if a year is a leap year\n"
                      "[3] Generate a calendar for a specific month\n"
                      "[4] Iterate over dates in a month\n"
                      "[5] Exit\n")
                choice = input("Enter your choice here: ")

                if choice == '1':
                    Calendar_Utility.find_weekday(self)

                elif choice == '2':
                    Calendar_Utility.check_leap_year(self)

                elif choice == '3':
                    Calendar_Utility.generate_calendar(self)

                elif choice == '4':
                    Calendar_Utility.iterate_dates(self)

                elif choice == '5':
                    print("\nThank you for using the program! \n"
                          "Exiting now...\n"
                          "...")
                    break

                else:
                    print("Sorry, that is an invalid input.\n"
                          ">> Please enter a valid number from the menu.\n")

            except ValueError:
                print("Sorry, that is an invalid input.\n"
                      ">> Please enter a valid number from the menu.\n")

if __name__ == "__main__":
    calendar_ut = Calendar_Utility()
    calendar_ut.run()
