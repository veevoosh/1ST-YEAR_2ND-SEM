class Airline:
    def __init__(self, airline_details, available_flights):
        self.airline_details = airline_details
        self.available_flights = available_flights


class Flight:
    def __init__(self, flight_num, airline, departure, des_airport, dep_time, arr_time, seat_capacity):
        self.flight_num = flight_num
        self.airline = airline
        self.departure = departure
        self.des_airport = des_airport
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.seat_capacity = seat_capacity


class DomesticFlight(Flight):
    def __init__(self, flight_num, airline, departure, des_airport, dep_time, arr_time, seat_capacity, domestic_fees):
        self.domestic_fees = domestic_fees
        super().__init__(flight_num, airline, departure, des_airport, dep_time, arr_time, seat_capacity)

    def __str__(self):
        return (f"Listing Domestic Flights for {airline}.\n"
                f"Flight Number: {self.flight_num}, From {self.departure} to {self.des_airport}\n"
                f"Departure time: {self.dep_time}, Arrival Time: {self.arr_time}\n"
                f"Seats Available: {self.seat_capacity}, Domestic Fee: {self.domestic_fees}G\n")


class InternationalFlight(Flight):
    def __init__(self, flight_num, airline, departure, des_airport, dep_time, arr_time, seat_capacity, int_fees):
        self.int_fees = int_fees
        super().__init__(flight_num, airline, departure, des_airport, dep_time, arr_time, seat_capacity)

    def __str__(self):
        return (f"Listing International Flights for {airline}.\n"
                f"Flight Number: {self.flight_num}, From {self.departure} to {self.des_airport}\n"
                f"Departure time: {self.dep_time}, Arrival Time: {self.arr_time}\n"
                f"Seats Available: {self.seat_capacity}, Domestic Fee: {self.int_fees}G\n")


class Passengers:
    def __init__(self, name, age, contact_info, passenger_id):
        self.name = name
        self.age = age
        self.contact_info = contact_info
        self.passenger_id = passenger_id

    def __str__(self):
        return (f"Thank you {self.name} for choosing {airline}!\n"
                f"Your Passenger ID is {self.passenger_id}.\n"
                f"Please use this ID for authentication in later transactions."
                f"We hope you enjoy your flight with us!\n")


class Reservation(Passengers, Flight):
    def __init__(self, name, passenger_id, flight_num, airline, departure, des_airport, dep_time, arr_time):
        Passengers.__init__(name, passenger_id)
        Flight.__init__(flight_num, airline, departure, des_airport, dep_time, arr_time)

    def __str__(self):
        return (f"Current Reservations for Passenger ID {self.passenger_id}:\n"
                f"Passenger: {self.name}, Flight: {self.flight_num}, From {self.departure} to {self.des_airport}\n"
                f"Status: Available\n")


def main():

    global name, passenger_id, flight_num, airline, departure, des_airport, dep_time, arr_time

    while True:
        print("Welcome to the Flight Reservation System!")
        print("[1] Choose an airline.")
        print("[2] View available flights.")
        print("[3] Book a flight.")
        print("[4] Cancel a flight booking.")
        print("[5] View reservations.")
        print("[6] Exit the system.")
        choice = input("Select your choice: ")
        print()

        if choice == '1':
            print("Select an Airline:")
            print("[1] Riptide Airlines")
            print("[2] Grandberry Flights")
            print("[3] Blackrose Travels")
            choice_2 = input("Select your choice: ")

            if choice_2 == '1':
                print("You have selected Riptide Airlines.\n")
                airline = "Riptide Airlines"
                main()

            elif choice_2 == '2':
                print("You have selected Grandberry Flights.\n")
                airline = "Grandberry Flights"
                main()

            elif choice_2 == '3':
                print("You have selected Blackrose Travels.\n")
                airline = "Blackrose Travels"
                main()

            else:
                print("Error! Please input a valid option.\n")
                main()

        elif choice == '2':
            print(f"Choose the type of flight to view for {airline}:")
            print("[1] Domestic Flights")
            print("[2] International Flights")
            flight_view = input("Select your choice: ")
            print()

            if flight_view == '1':
                flight_num = "JRWI20"
                departure = "Canella Airport"
                des_airport = "Edison Royal Airport"
                dep_time = "8:00am"
                arr_time = "9:00am"
                seat_capacity = 150
                domestic_fees = 10
                domestic_flight = DomesticFlight(flight_num, airline, departure, des_airport, dep_time, arr_time, seat_capacity, domestic_fees)
                print(domestic_flight)
                print()

            elif flight_view == '2':
                flight_num = "FATE01"
                departure = "Canella Airport"
                des_airport = "Undersea Corale Airport"
                dep_time = "10:00am"
                arr_time = "1:00pm"
                seat_capacity = 50
                int_fees = 25
                international_flight = InternationalFlight(flight_num, airline, departure, des_airport, dep_time, arr_time,
                                                 seat_capacity, int_fees)
                print(international_flight)
                print()

            else:
                print("Error! Please input a valid option.")
                main()

        elif choice == '3':
            user_num = input("Enter Flight Number: ")
            if user_num == "JRWI20":
                name = input("Enter Passenger Name: ")
                age = input("Enter Your Age: ")
                contact_info = input("Enter Your Mobile Number For Contact: ")
                passenger_id = input("Enter Passenger ID: ")
                print("Booking successful! Total fee: 20G (10G for ticket, 10G for domestic flight.")
                passenger = Passengers(name, age, contact_info, passenger_id)
                print(passenger)
                print()
                main()

            elif user_num == "FATE01":
                name = input("Enter Passenger Name: ")
                age = input("Enter Your Age: ")
                contact_info = input("Enter Your Mobile Number For Contact: ")
                passenger_id = input("Enter Passenger ID: ")
                print("Booking successful! Total fee: 35G (10G for ticket, 25G for international flight.")
                passenger = Passengers(name, age, contact_info, passenger_id)
                print(passenger)
                print()
                main()

            else:
                print("Error! Please input a valid option.")
                main()

        elif choice == '4':
            user_num = input("Enter Flight Number: ")
            if user_num == "JRWI20":
                user_id = input("Enter Passenger ID: ")
                print(f"Booking cancelled for {user_id} on Flight {user_num}.")
                print()
                main()

            elif user_num == "FATE01":
                user_id = input("Enter Passenger ID: ")
                print(f"Booking cancelled for {user_id} on Flight {user_num}.")
                del passenger_id
                print()
                main()

            else:
                print("Error! Please input a valid option.")
                print()
                main()

        elif choice == '5':
            reservations = Reservation(name, passenger_id, flight_num, airline, departure, des_airport, dep_time, arr_time)
            print(reservations)

        elif choice == '6':
            print("Exiting the program...\n"
                  "Thank you for using the Flight Reservation System!")
            print()
            break

        else:
            print("Error! Please input a valid option.")
            print()
            main()

if __name__ == "__main__":
    main()
