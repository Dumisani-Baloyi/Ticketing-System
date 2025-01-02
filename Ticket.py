import json
from datetime import datetime

# File to store tickets
TICKET_FILE = "tickets.json"

# Load tickets from file
def load_tickets():
    try:
        with open(TICKET_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tickets to file
def save_tickets(tickets):
    with open(TICKET_FILE, "w") as file:
        json.dump(tickets, file, indent=4)

# Create a new ticket
def create_ticket():
    tickets = load_tickets()
    title = input("Enter the ticket title: ")
    description = input("Enter the ticket description: ")
    priority = input("Enter priority (low/medium/high): ").lower()
    
    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "open",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": None
    }
    tickets.append(ticket)
    save_tickets(tickets)
    print(f"Ticket created successfully with ID {ticket['id']}.")

# View all tickets
def view_tickets():
    tickets = load_tickets()
    if not tickets:
        print("No tickets found.")
        return

    for ticket in tickets:
        print(f"ID: {ticket['id']}, Title: {ticket['title']}, Priority: {ticket['priority']}, Status: {ticket['status']}, Created At: {ticket['created_at']}")

# Update a ticket
def update_ticket():
    tickets = load_tickets()
    ticket_id = int(input("Enter the ticket ID to update: "))
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)

    if ticket:
        print(f"Current Status: {ticket['status']}")
        new_status = input("Enter new status (open/in progress/closed): ").lower()
        if new_status in ["open", "in progress", "closed"]:
            ticket["status"] = new_status
            ticket["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tickets(tickets)
            print(f"Ticket ID {ticket_id} updated successfully.")
        else:
            print("Invalid status.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

# Delete a ticket
def delete_ticket():
    tickets = load_tickets()
    ticket_id = int(input("Enter the ticket ID to delete: "))
    tickets = [t for t in tickets if t["id"] != ticket_id]
    save_tickets(tickets)
    print(f"Ticket ID {ticket_id} deleted successfully.")

# Menu
def menu():
    while True:
        print("\n--- Ticketing System ---")
        print("1. Create Ticket")
        print("2. View All Tickets")
        print("3. Update Ticket Status")
        print("4. Delete Ticket")
        print("5. Exit")

        choice = input("Select an option (1-5): ")
        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            delete_ticket()
        elif choice == "5":
            print("Exiting the ticketing system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
