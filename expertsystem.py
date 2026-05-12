# -------- INTRO --------
def intro():
    print("\nMEDICAL EXPERT SYSTEM")


# -------- PATIENT ANALYSIS --------
def analyze():
    print("\nAnswer in yes/no")

    fever = input("Fever: ").lower()
    cough = input("Cough: ").lower()
    chest = input("Chest pain: ").lower()
    stomach = input("Stomach pain: ").lower()
    injury = input("Injury: ").lower()
    sugar = input("High sugar: ").lower()

    print("\n--- RESULT ---")

    # 1. Flu
    if fever=="yes" and cough=="yes":
        print("Flu -> General Doctor")

    # 2. Heart Problem
    elif chest=="yes":
        print("Heart Problem -> Cardiologist")

    # 3. Digestion Issue
    elif stomach=="yes":
        print("Digestion Problem -> Gastro")

    # 4. Injury / Fracture
    elif injury=="yes":
        print("Fracture -> Orthopedic")

    # 5. Diabetes
    elif sugar=="yes":
        print("Diabetes -> Endocrinologist")

    # 6. Fever Only (General Infection)
    elif fever=="yes":
        print("General Infection -> Physician")

    else:
        print("No major issue. Stay healthy!")


# -------- OTHER OPTIONS --------
def emergency():
    print("Call 108 | 24x7 Emergency")

def facilities():
    print("OPD | ICU | Lab | Ambulance")

def about():
    print("Rule-based Expert System")


# -------- MAIN MENU --------
def system():
    while True:
        print("\n1.Analysis 2.Emergency 3.Facilities 4.About 5.Exit")
        ch = input("Choice: ")

        if ch=="1":
            analyze()
        elif ch=="2":
            emergency()
        elif ch=="3":
            facilities()
        elif ch=="4":
            about()
        elif ch=="5":
            print("Thank You!")
            break
        else:
            print("Invalid choice")


# -------- DRIVER --------
intro()
system()