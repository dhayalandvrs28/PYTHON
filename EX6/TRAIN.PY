class Train:
    def __init__(self, train_number, source, destination, seats):
        self.train_number = train_number
        self.source = source
        self.destination = destination
        self.seats = seats  # Total number of seats
        self.booked_seats = 0  # Number of booked seats

    def available_seats(self):
        return self.seats - self.booked_seats

    def book_ticket(self, number_of_tickets):
        if number_of_tickets <= self.available_seats():
            self.booked_seats += number_of_tickets
            return True
        else:
            return False


class Ticket:
    def __init__(self, train, passenger_name, number_of_tickets):
        self.train = train
        self.passenger_name = passenger_name
        self.number_of_tickets = number_of_tickets

    def __str__(self):
        return (f"Ticket for {self.passenger_name}:\n"
                f"Train Number: {self.train.train_number}\n"
                f"From: {self.train.source} To: {self.train.destination}\n"
                f"Number of Tickets: {self.number_of_tickets}\n")


class TrainBookingSystem:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def display_trains(self):
        print("Available Trains:")
        for train in self.trains:
            print(f"Train Number: {train.train_number}, From: {train.source}, To: {train.destination}, Available Seats: {train.available_seats()}")

    def book_ticket(self, train_number, passenger_name, number_of_tickets):
        for train in self.trains:
            if train.train_number == train_number:
                if train.book_ticket(number_of_tickets):
                    ticket = Ticket(train, passenger_name, number_of_tickets)
                    print(ticket)
                    return
                else:
                    print("Not enough available seats.")
                    return
        print("Train not found.")


# Initialize system and add trains
system = TrainBookingSystem()
system.add_train(Train("101", "CityA", "CityB", 100))
system.add_train(Train("102", "CityB", "CityC", 50))
system.add_train(Train("103", "CityA", "CityC", 75))

# Command line interface loop
while True:
    system.display_trains()
    train_number = input("Enter Train Number to book a ticket (or 'exit' to quit): ")
    if train_number.lower() == 'exit':
        break
    passenger_name = input("Enter your name: ")
    number_of_tickets = int(input("Enter number of tickets: "))
    system.book_ticket(train_number, passenger_name, number_of_tickets)
