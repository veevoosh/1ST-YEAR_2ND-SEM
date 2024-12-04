import datetime
import pytz


class DateTime_Utility:

    @staticmethod
    def parse_datetime(self):
        try:
            user_dt = input("\nEnter a date/time (MM/DD/YYYY HH:MM): ")
            dt_obj = datetime.datetime.strptime(user_dt, '%m/%d/%Y %H:%M')
            dt_str = datetime.datetime.strftime(dt_obj, '%B %d, %Y %I:%M %p')
            print(f"\n >> Parsed Date/Time: {dt_str}\n")
            return

        except ValueError:
            print("\nSorry, that is an invalid input.\n"
                  ">> Please enter a valid date/time.\n")
            return

    @staticmethod
    def convert_timezone(self):
        try:
            user_dt = input("\nEnter the original date/time (MM/DD/YYYY HH:MM:SS): ")
            dt_obj = datetime.datetime.strptime(user_dt, '%m/%d/%Y %H:%M:%S')

            orig_dt = input("\nWhat is the original timezone?\n"
                            "[1] GMT\n"
                            "[2] EST\n"
                            "Enter your choice here: ")

            target_dt = input("\nWhat is the target timezone?\n"
                              "[1] PDT\n"
                              "[2] IST\n"
                              "Enter your choice here: ")

            if orig_dt == '1':
                GMT_tz = pytz.timezone('GMT')
                dt_GMT = GMT_tz.localize(dt_obj)

                if target_dt == '1':
                    dt_PDT = dt_GMT.astimezone(pytz.timezone('PST8PDT'))
                    converted_tz = datetime.datetime.strftime(dt_PDT, '%B %d, %Y %I:%S %p %Z')
                    print(f"\n >> Converted Date/Time: {converted_tz}\n")
                    return

                elif target_dt == '2':
                    dt_IST = dt_GMT.astimezone(pytz.timezone('Asia/Kolkata'))
                    converted_tz = datetime.datetime.strftime(dt_IST, '%B %d, %Y %I:%S %p %Z')
                    print(f"\n >> Converted Date/Time: {converted_tz}\n")
                    return

                else:
                    print("\nSorry, that is an invalid input.\n"
                          ">> Please try again.\n")
                    return

            elif orig_dt == '2':
                EST_tz = pytz.timezone('EST')
                dt_EST = EST_tz.localize(dt_obj)

                if target_dt == '1':
                    dt_PDT = dt_EST.astimezone(pytz.timezone('PST8PDT'))
                    converted_tz = datetime.datetime.strftime(dt_PDT, '%B %d, %Y %I:%S %p %Z')
                    print(f"\n >> Converted Date/Time: {converted_tz}\n")
                    return

                elif target_dt == '2':
                    dt_IST = dt_EST.astimezone(pytz.timezone('Asia/Kolkata'))
                    converted_tz = datetime.datetime.strftime(dt_IST, '%B %d, %Y %I:%S %p %Z')
                    print(f"\n >> Converted Date/Time: {converted_tz}\n")
                    return

                else:
                    print("Sorry, that is an invalid input.\n"
                          ">> Please try again.\n")
                    return

            else:
                print("Sorry, that is an invalid input.\n"
                      ">> Please try again.\n")
                return

        except ValueError:
            print("\nSorry, that is an invalid input.\n"
                  ">> Please enter a valid date/time.\n")
            return

    @staticmethod
    def perform_date_arith(self):
        try:
            user_dt = input("\nEnter a date (MM/DD/YYYY): ")
            dt_obj = datetime.datetime.strptime(user_dt, '%m/%d/%Y')
            add_or_sub = input("\nWhat operation would you like to do?\n"
                               "[1] Add\n"
                               "[2] Subtract\n"
                               "\nEnter your choice here: ")

            if add_or_sub == '1':
                day_add = int(input("\nEnter the number of day/s to add: "))
                tdelta = datetime.timedelta(days=day_add)
                add_result = dt_obj + tdelta
                converted_tz = datetime.datetime.strftime(add_result, '%B %d, %Y')
                print(f"\n >> Resultant Date: {converted_tz}\n")
                return

            elif add_or_sub == '2':
                day_sub = int(input("\nEnter the number of day/s to subtract: "))
                tdelta = datetime.timedelta(days=day_sub)
                sub_result = dt_obj - tdelta
                converted_tz = datetime.datetime.strftime(sub_result, '%B %d, %Y')
                print(f"\n >> Resultant Date: {converted_tz}\n")
                return

            else:
                print("Sorry, that is an invalid input.\n"
                      ">> Please try again.\n")
                return

        except ValueError:
            print("\nSorry, that is an invalid input.\n"
                  ">> Please enter a valid date/time.\n")
            return

    @staticmethod
    def format_dt(self):
        try:
            user_dt = input("\nEnter a date/time (YYYY/MM/DD HH:MM): ")
            dt_obj = datetime.datetime.strptime(user_dt, '%Y/%m/%d %H:%M')
            format = input("\nChoose a format below:\n"
                           "[1] MM/DD/YYYY\n"
                           "[2] DD/MM/YYYY\n"
                           "[3] YYYY/MM/DD\n"
                           "\nEnter your choice here: ")

            if format == '1':
                dt_str = datetime.datetime.strftime(dt_obj, '%m/%d/%Y %I:%M %p')
                print(f"\n >> Formatted Date/Time: {dt_str}\n")
                return

            elif format == '2':
                dt_str = datetime.datetime.strftime(dt_obj, '%d/%m/%Y %I:%M %p')
                print(f"\n >> Formatted Date/Time: {dt_str}\n")
                return

            elif format == '3':
                dt_str = datetime.datetime.strftime(dt_obj, '%Y/%m/%d %I:%M %p')
                print(f"\n >> Formatted Date/Time: {dt_str}\n")
                return

            else:
                print("Sorry, that is an invalid input.\n"
                      ">> Please try again.\n")
                return

        except ValueError:
            print("\nSorry, that is an invalid input.\n"
                  ">> Please enter a valid date/time.\n")
            return

    def run(self):
        while True:
            try:
                print("Welcome to the Python DateTime Utility!\n"
                      "\nWhat would you like to do?\n"
                      "[1] Parse Date/Time\n"
                      "[2] Convert Timezones\n"
                      "[3] Perform Date Arithmetic\n"
                      "[4] Format Date / Time\n"
                      "[5] Exit\n")
                choice = input("Enter your choice here: ")

                if choice == '1':
                    DateTime_Utility.parse_datetime(self)

                elif choice == '2':
                    DateTime_Utility.convert_timezone(self)

                elif choice == '3':
                    DateTime_Utility.perform_date_arith(self)

                elif choice == '4':
                    DateTime_Utility.format_dt(self)

                elif choice == '5':
                    print("Thank you for using the program! \n"
                          "Exiting...\n"
                          "...")
                    break

                else:
                    print("Sorry, that is an invalid input.\n"
                          ">> Please enter a valid number from the menu.\n")

            except ValueError:
                print("Sorry, that is an invalid input.\n"
                      ">> Please enter a valid number from the menu.\n")


if __name__ == "__main__":
    datetime_ut = DateTime_Utility()
    datetime_ut.run()
