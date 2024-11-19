def calculate_average_rainfall():
    print("### Average Rainfall Calculation ###")
    total_rainfall = 0
    total_months = 0

    # Ask the user for the number of years
    years = int(input("\nEnter the number of years: "))

    # Outer loop for each year
    for year in range(1, years + 1):
        print(f"\nYear {year}")
        # Inner loop for each month
        for month in range(1, 13):
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            total_rainfall += rainfall
            total_months += 1

    # Calculate average rainfall
    average_rainfall = total_rainfall / total_months

    # Display results
    print(f"\nTotal months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")


def calculate_bookstore_points():
    print("\n### CSU Global Bookstore Points ###")
    # Ask the user for the number of books purchased
    books_purchased = int(input("\nEnter the number of books purchased this month: "))

    # Determine points earned
    if books_purchased == 0:
        points = 0
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 8:
        points = 60
    else:
        points = 0  # Catch-all case for other invalid inputs (if any)

    # Display the number of points awarded
    print(f"Points awarded: {points}")


def main():
    print("Welcome! Please select an option:")
    print("1. Calculate Average Rainfall")
    print("2. Calculate Bookstore Points")
    choice = int(input("\nEnter your choice (1 or 2): "))

    if choice == 1:
        calculate_average_rainfall()
    elif choice == 2:
        calculate_bookstore_points()
    else:
        print("Invalid choice. Please run the program again.")

# Run the main program
if __name__ == "__main__":
    main()
