from collections import deque

# Node for Linked List (Confirmed bookings)
class PassengerNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class TicketBookingSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked_count = 0
        self.head = None  # Linked list head
        self.waiting_queue = deque()  # Waiting list queue

    def book_ticket(self, name):
        if self.booked_count < self.total_seats:
            new_passenger = PassengerNode(name)
            if not self.head:
                self.head = new_passenger
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_passenger
            self.booked_count += 1
            print(f"\n✅ Ticket confirmed for {name}")
        else:
            self.waiting_queue.append(name)
            print(f"\n⏳ No seats available. {name} added to waiting list.")

    def cancel_ticket(self, name):
        if not self.head:
            print("\n⚠️ No bookings to cancel.")
            return

        temp = self.head
        prev = None
        found = False

        while temp:
            if temp.name == name:
                found = True
                break
            prev = temp
            temp = temp.next

        if not found:
            print(f"\n❌ No booking found for {name}.")
            return

        # Remove the node from linked list
        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next
        self.booked_count -= 1
        print(f"\n❎ Booking cancelled for {name}")

        # Allocate seat to next waiting passenger
        if self.waiting_queue:
            next_passenger = self.waiting_queue.popleft()
            self.book_ticket(next_passenger)
            print(f"🎟️ Seat allocated to waiting passenger: {next_passenger}")

    def display_confirmed(self):
        if not self.head:
            print("\n🚫 No confirmed passengers.")
            return
        temp = self.head
        print("\n📋 Confirmed Passengers:")
        while temp:
            print(f" - {temp.name}")
            temp = temp.next

    def display_waiting(self):
        if not self.waiting_queue:
            print("\n🚫 No one in waiting list.")
        else:
            print("\n⌛ Waiting List:")
            for person in self.waiting_queue:
                print(f" - {person}")


# ---------------------- MENU-DRIVEN PROGRAM ----------------------
system = TicketBookingSystem(total_seats=3)

while True:
    print("\n====== Ticket Booking System ======")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Show Confirmed Passengers")
    print("4. Show Waiting List")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter passenger name: ")
        system.book_ticket(name)

    elif choice == '2':
        name = input("Enter passenger name to cancel: ")
        system.cancel_ticket(name)

    elif choice == '3':
        system.display_confirmed()

    elif choice == '4':
        system.display_waiting()

    elif choice == '5':
        print("👋 Exiting the system. Thank you!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
