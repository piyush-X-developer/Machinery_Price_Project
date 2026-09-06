# Agricultural Machinery Price Finder
# A beginner-friendly Python project for checking estimated machinery prices.

MACHINES = {
    "1": ("Straw reaper", "₹3.2–4.0 lakh"),
    "2": ("Paddy cleaner", "₹45,000–₹2 lakh+"),
    "3": ("Rotavator", "₹50,000–₹3 lakh"),
    "4": ("Harrow", "₹45,000–₹3.5 lakh"),
    "5": ("Potato seeder", "₹1.25–₹7.5 lakh"),
    "6": ("Tiller", "₹1.6–₹3.1 lakh"),
    "7": ("Small tiller", "₹10,000–₹80,000+"),
}


def show_machines():
    """Display the available agricultural machines."""
    print("\nALL MACHINES")
    print("=" * 40)
    for number, (name, _) in MACHINES.items():
        print(f"{number}. {name}")


def find_machine(choice):
    """Find a machine by number or name (case-insensitive)."""
    choice = choice.strip().lower()

    if choice in MACHINES:
        return MACHINES[choice]

    for name, price in MACHINES.values():
        if choice == name.lower():
            return name, price

    return None


def main():
    """Run the machinery price finder."""
    print("AGRICULTURAL MACHINERY PRICE FINDER")

    while True:
        show_machines()
        choice = input("\nEnter machine name or number (or 'q' to quit): ")

        if choice.strip().lower() == "q":
            print("Thanks for using the Machinery Price Finder!")
            break

        machine = find_machine(choice)

        if machine:
            name, price = machine
            print(f"\n{name}: {price}")
        else:
            print("\nMachine not found. Please enter a listed number or exact machine name.")


if __name__ == "__main__":
    main()
