# Simple program to add and display data in table format

# List to store rows (each row is a list of values)
table = []

def add_row():
    # For example, let's say our table has 3 columns: Name, Age, City
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    table.append([name, age, city])
    print("Row added!\n")

def display_table():
    if not table:
        print("No data to display.\n")
        return

    # Print header
    print(f"{'Name':<15} {'Age':<5} {'City':<15}")
    print("-" * 37)

    # Print rows
    for row in table:
        print(f"{row[0]:<15} {row[1]:<5} {row[2]:<15}")
    print()

def main():
    while True:
        print("1. Add data")
        print("2. Display table")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_row()
        elif choice == '2':
            display_table()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()

