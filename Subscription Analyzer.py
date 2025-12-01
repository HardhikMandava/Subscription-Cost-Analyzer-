def print_menu():
  print("\n=== Subscription Cost Analyzer ===")
  print("1. Add Subscription")
  print("2. View Subscription")
  pritnt("3. Show totals and savings suggestions")
  print("4. Remove a Subscription")
  print(5. Exit)

def add_subscription(subscriptions):
  name = input("Enter subscription name (e.g., Netflix): ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        price = float(input("Enter price (e.g., 15.99): "))
        if price <= 0:
            print("Price must be greater than 0.")
            return
    except ValueError:
        print("Invalid price.")
        return

    period = input("Is this billed monthly or yearly? (m/y): ").strip().lower()
    if period == "m":
        billing_period = "monthly"
    elif period == "y":
        billing_period = "yearly"
    else:
        print("Invalid choice. Use 'm' or 'y'.")
        return

    subscriptions.append({
        "name": name,
        "price": price,
        "billing_period": billing_period
    })
    print(f"Added subscription: {name} ({billing_period}, ${price:.2f})")
def view_subscriptions(subscriptions):
    if not subscriptions:
        print("\nNo subscriptions added yet.")
        return

    print("\nCurrent subscriptions:")
    print("{:<3} {:<20} {:<10} {:<10}".format("#", "Name", "Billing", "Price"))
    print("-" * 50)
    for i, sub in enumerate(subscriptions, start=1):
        print("{:<3} {:<20} {:<10} ${:<10.2f}".format(
            i, sub["name"], sub["billing_period"], sub["price"]
        ))


def calculate_totals(subscriptions, show_details=True):
    total_monthly = 0.0
    total_yearly = 0.0
    costs = []

    for sub in subscriptions:
        if sub["billing_period"] == "monthly":
            monthly = sub["price"]
            yearly = sub["price"] * 12
        else:  # yearly
            yearly = sub["price"]
            monthly = sub["price"] / 12

        total_monthly += monthly
        total_yearly += yearly

        costs.append({
            "name": sub["name"],
            "monthly": monthly,
            "yearly": yearly
        })

    if show_details:
        print(f"\nTotal monthly cost: ${total_monthly:.2f}")
        print(f"Total yearly cost:  ${total_yearly:.2f}")

        if costs:
            # find most expensive by monthly cost
            costs.sort(key=lambda c: c["monthly"], reverse=True)
            top = costs[0]
            print(
                f"\nIf you cancelled '{top['name']}', you would save "
                f"${top['monthly']:.2f} per month (${top['yearly']:.2f} per year)."
            )
        else:
            print("No subscriptions to analyze.")

    return total_monthly, total_yearly, costs


def remove_subscription(subscriptions):
    if not subscriptions:
        print("\nNo subscriptions to remove.")
        return

    view_subscriptions(subscriptions)
    try:
        index = int(input("Enter the # of the subscription to remove: "))
        if 1 <= index <= len(subscriptions):
            removed = subscriptions.pop(index - 1)
            print(f"Removed subscription: {removed['name']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    subscriptions = []

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_subscription(subscriptions)
        elif choice == "2":
            view_subscriptions(subscriptions)
        elif choice == "3":
            calculate_totals(subscriptions)
        elif choice == "4":
            remove_subscription(subscriptions)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1–5.")


if __name__ == "__main__":
    main()
