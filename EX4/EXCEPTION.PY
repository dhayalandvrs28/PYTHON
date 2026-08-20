class InvalidPriceError(Exception):
    """Custom exception for invalid ticket prices."""
    pass

class Ticket:
    total_sold = 0
    total_seats = 100

    def __init__(self, name, train, seat, price):
        self.name = name
        self.train = train
        self.seat = seat
        self.price = price
        Ticket.total_sold += 1

    def details(self):
        return (f"Name: {self.name}\n"
                f"Train: {self.train}\n"
                f"Seat: {self.seat}\n"
                f"Price: ${self.price:.2f}")

    @classmethod
    def remaining_seats(cls):
        return cls.total_seats - cls.total_sold

    @staticmethod
    def total_tickets():
        return Ticket.total_sold


while True:
    if Ticket.remaining_seats() <= 0:
        print("No more seats available.")
        break

    name = input("Passenger name: ")
    train = input("Train number: ")
    seat = input("Seat number: ")

    # Exception handling for ticket price input
    while True:
        try:
            price = float(input("Ticket price: "))
            if price < 0:
                raise InvalidPriceError("Price cannot be negative.")
            break  # Exit the loop if the price is valid
        except ValueError:
            print("Invalid input for price: Please enter a valid number.")
        except InvalidPriceError as e:
            print(e)

    ticket = Ticket(name, train, seat, price)

    print("\nTicket Details:")
    print(ticket.details())
    print("-----")

    another = input("Create another ticket? (yes/no): ").strip().lower()
    if another != 'yes':
        break

print(f"\nTotal tickets sold: {Ticket.total_tickets()}")
print(f"Remaining seats: {Ticket.remaining_seats()}") 
