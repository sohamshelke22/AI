# ---------------- INTRO ----------------
def intro():
    print("=" * 50)
    print("     WELCOME TO K's RESTAURANT CHATBOT")
    print("=" * 50)


# ---------------- MENU ----------------
def menu():
    print("\nMENU")
    print("Pizza - Rs.350 | Burger - Rs.250 | Pasta - Rs.300")
    print("Ice Cream - Rs.120 | Coffee - Rs.140")


# ---------------- PRICE ----------------
def price():
    print("\nAverage Prices: Pizza 350, Burger 250, Pasta 300, Coffee 140")

    budget = int(input("Enter your budget: "))

    if budget < 500:
        print("Suggested: Burger, Fries, Coffee")
    elif budget <= 1500:
        print("Suggested: Pizza, Pasta, Dessert")
    else:
        print("Suggested: Full Meal + Dessert + Drinks")


# ---------------- RESERVATION ----------------
def reserve():
    name = input("Name: ")
    persons = input("Persons: ")
    date = input("Date: ")
    time = input("Time: ")

    print("\nReservation Done!")
    print(name, persons, date, time)


# ---------------- OTHER INFO ----------------
def contact():
    print("Phone: 9876543210 | Email: ksrestaurant@gmail.com")

def timing():
    print("11 AM - 10 PM (Weekdays), 10 AM - 11 PM (Weekends)")

def offers():
    print("Offers: Buy1Get1 Pizza, 20% off Pasta")

def about():
    print("K's Restaurant - Since 2015 | Good Food & Service")

def feedback():
    name = input("Name: ")
    rating = input("Rating (1-5): ")
    print("Thanks", name)


# ---------------- CHATBOT ----------------
def chatbot():
    while True:
        msg = input("\nYou: ").lower()

        if "menu" in msg:
            menu()

        elif "price" in msg or "cost" in msg:
            price()

        elif "book" in msg or "table" in msg:
            reserve()

        elif "contact" in msg:
            contact()

        elif "time" in msg or "open" in msg:
            timing()

        elif "offer" in msg:
            offers()

        elif "about" in msg:
            about()

        elif "feedback" in msg:
            feedback()

        elif "hello" in msg or "hi" in msg:
            print("Hello! Welcome to K's Restaurant")

        elif "exit" in msg:
            print("Thank you! Visit again.")
            break

        else:
            print("Sorry! Try: menu, price, book, contact, offers, exit")


# ---------------- MAIN ----------------
intro()
chatbot()