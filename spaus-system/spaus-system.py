import os
from datetime import datetime
import calendar

class SPAUS:
    def __init__(self, filename='spaus_data.txt'):
        self.apps = {}
        self.filename = filename
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, 'r') as file:
                app = None
                for line in file:
                    line = line.strip()
                    if line.startswith("App:"):
                        app = line[4:].strip()
                        self.apps[app] = []
                    elif app:
                        parts = line.split('|')
                        entry = {'Date': parts[0], 'Version': parts[1], 'Remarks': parts[-1]}
                        if len(parts) == 4:
                            entry['Type'] = parts[2]
                        self.apps[app].append(entry)
        except Exception as e:
            print("\n>> Error loading data:", e)

    def save_data(self):
        try:
            with open(self.filename, 'w') as file:
                for app, updates in self.apps.items():
                    file.write(f"App: {app}\n")
                    for update in updates:
                        line = f"{update['Date']}|{update['Version']}"
                        if 'Type' in update:
                            line += f"|{update['Type']}"
                        line += f"|{update['Remarks']}\n"
                        file.write(line)
        except Exception as e:
            print("\n>> Error saving data:", e)

    def add_update(self, app, date, version, remarks):
        if app not in self.apps:
            self.apps[app] = []

        self.apps[app].append({'Date': date, 'Version': version, 'Remarks': remarks})
        self.save_data()

    def add_patch(self, app, date, version, type, remarks):
        if app not in self.apps:
            self.apps[app] = []

        self.apps[app].append({'Date': date, 'Version': version, 'Type': type, 'Remarks': remarks})
        self.save_data()

    def display_all(self):
        try:
            if not self.apps:
                print("\n>> No updates or patches recorded yet.")
                return

            for app, updates in self.apps.items():
                print("\n>> App Name:", app)
                for update in updates:
                    if 'Type' in update:
                        print("\nLog of Software Patches")
                        print("Date:", update['Date'])
                        print("Version:", update['Version'])
                        print("Type:", update['Type'])
                        print("Remarks:", update['Remarks'])
                    else:
                        print("\nLog of Software Updates")
                        print("Date:", update['Date'])
                        print("Version:", update['Version'])
                        print("Remarks:", update['Remarks'])
                print()
        except Exception as i:
            print("\n>> Error displaying updates and patches:", i)

    def search_updates_patches(self, app, key, value):
        if app in self.apps:
            updates = self.apps[app]
            found = False

            for update in updates:
                if key in update and update[key] == value:
                    found = True
                    if 'Type' in update:
                        print("\n>> App Name:", app, "| Date:", update['Date'], "| Version:", update['Version'],
                              "| Type:",
                              update['Type'], "| Remarks:", update['Remarks'])
                    else:
                        print("\n>> App Name:", app, "| Date:", update['Date'], "| Version:", update['Version'],
                              "| Remarks:", update['Remarks'])
            if not found:
                print("\n>> No update or patch found for the given", key, "in the specified app.")
        else:
            print("\n>> No updates found for the specified app.")

    def delete_updates_patches(self):
        self.load_data()

        if not self.apps:
            print("\n>> No updates or patches recorded yet.")
            return

        print("\n>> List of Software Patches and Updates")
        for i, (app, updates) in enumerate(self.apps.items()):
            print(f"\n {i + 1}. {app}")
            for j, update in enumerate(updates):
                print(
                    f"   {j + 1}. Date: {update['Date']} | Version: {update['Version']} | Remarks: {update['Remarks']}")

        while True:
            try:
                choice = int(input("\nSelect the app: "))

                if 1 <= choice <= len(self.apps):
                    app = list(self.apps.keys())[choice - 1]
                    update_choice = int(input(f"\nSelect an update/patch log to delete for {app}: "))
                    if 1 <= update_choice <= len(self.apps[app]):
                        del self.apps[app][update_choice - 1]
                        self.save_data()  # Save the updated data back to the file
                        print("\n>> Software log deleted successfully!")
                        break
                    else:
                        print("\n>> Invalid choice.")
                else:
                    print("\n>> Invalid choice.")
            except ValueError:
                print("\n>> Invalid choice. Please enter a number.")

    def set_future_plans(self, app, date, version, notes):
        today = datetime.today().date()
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()

        if date_obj <= today:
            print("\n>> Invalid date. Please enter a future date.")
            return
        self.add_update(app, date, version, notes)

def main():
    spaus = SPAUS()

    while True:
        try:
            a = """
                    ▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
                    ▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
                    ▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
                    ▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
                    ░░░░▄▄███▄▄░░░░░█████░
                """
            print(a)
            print("\n▂▃▅▇█▓▒░ Welcome to Software Patches and Updates System ░▒▓█▇▅▃▂")
            print("\n➠ 1. Add Update")
            print("➠ 2. Add Patch")
            print("➠ 3. Display All Updates and Patches")
            print("➠ 4. Search by Date")
            print("➠ 5. Search by Version")
            print("➠ 6. Delete a Software Update/Patch Log")
            print("➠ 7. Set Future Update")
            print("➠ 8. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                app = input("\nEnter App Name: ")
                date = input("Enter Date of Update (YYYY-MM-DD): ")
                version = input("Enter Version: ")
                remarks = input("Enter Remarks: ")
                spaus.add_update(app, date, version, remarks)
                print("\n>> Update logged successfully!")

            elif choice == '2':
                app = input("\nEnter App Name: ")
                date = input("Enter Date of Patch (YYYY-MM-DD): ")
                version = input("Enter Version: ")
                type = input("Enter Patch Type: ")
                remarks = input("Enter Remarks: ")
                spaus.add_patch(app, date, version, type, remarks)
                print("\n>> Patch logged successfully!")

            elif choice == '3':
                spaus.display_all()

            elif choice == '4':
                app = input("\nEnter App Name: ")
                year = int(input("Year (YYYY): "))
                month = int(input("Month (MM): "))
                c = calendar.Calendar()

                print("\n>> Dates in the specified month with updates or patches:")
                available_dates = set()
                for update in spaus.apps.get(app, []):
                    update_date = datetime.strptime(update['Date'], "%Y-%m-%d").date()
                    if update_date.year == year and update_date.month == month:
                        available_dates.add(update_date)
                all_dates_in_month = list(c.itermonthdates(year, month))

                for date in all_dates_in_month:
                    if date.month == month and date in available_dates:
                        print(date.strftime('%Y-%m-%d'))
                value = input("\nEnter Date (YYYY-MM-DD): ")
                spaus.search_updates_patches(app, 'Date', value)

            elif choice == '5':
                app = input("\nEnter App Name: ")
                version = input("Enter Version: ")
                spaus.search_updates_patches(app, 'Version', version)

            elif choice == '6':
                spaus.delete_updates_patches()

            elif choice == '7':
                app = input("\nEnter App Name: ")
                date = input("Set Future Date of Update (YYYY-MM-DD): ")
                version = input("Enter Version: ")
                notes = input("Enter Notes: ")
                spaus.set_future_plans(app, date, version, notes)
                print("\n>> Future update set successfully!")

            elif choice == '8':
                print("\n>> Exiting the program...")
                break

            else:
                print("\n>> Invalid choice. Please enter a valid option.")

        except Exception as i:
            print("\n>> An error occurred:", i)


if __name__ == "__main__":
    main()
